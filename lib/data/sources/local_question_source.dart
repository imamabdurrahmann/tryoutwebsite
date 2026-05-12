import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';
import '../../core/constants/app_constants.dart';
import '../models/question.dart';

/// Fungsi yang jalan di Background Isolate.
/// Parsing JSON string → List<Question> di thread terpisah.
List<Question> _parseJsonInBackground(String jsonString) {
  final List<dynamic> jsonList = jsonDecode(jsonString) as List<dynamic>;
  return jsonList.map((json) => Question.fromJson(json as Map<String, dynamic>)).toList();
}

class LocalQuestionSource {
  /// Memory cache to prevent reload from JSON asset every access
  static List<Question>? _memoryCache;
  static DateTime? _cacheTimestamp;
  static const _cacheTTL = Duration(minutes: 30);
  static String _cachedPackageId = '';

  /// Check if cache is valid based on package ID and TTL
  static bool get _isCacheValid =>
      _memoryCache != null &&
      _cacheTimestamp != null &&
      _cachedPackageId == _packageId &&
      DateTime.now().difference(_cacheTimestamp!) < _cacheTTL;

  /// packageId: '1' (default), '2', or '3'
  static String _packageId = '1';

  static void setPackage(String packageId) {
    final newPackageId = (packageId == '2' || packageId == '3') ? packageId : '1';
    if (newPackageId != _packageId) {
      clearCache(); // Clear cache when switching packages
    }
    _packageId = newPackageId;
  }

  /// Clear the memory cache
  static void clearCache() {
    _memoryCache = null;
    _cacheTimestamp = null;
    _cachedPackageId = '';
  }

  String _twkPath() {
    if (_packageId == '2') return AppConstants.twkJsonPath2;
    if (_packageId == '3') return AppConstants.twkJsonPath3;
    return AppConstants.twkJsonPath;
  }
  String _tiuPath() {
    if (_packageId == '2') return AppConstants.tiuJsonPath2;
    if (_packageId == '3') return AppConstants.tiuJsonPath3;
    return AppConstants.tiuJsonPath;
  }
  String _tkpPath() {
    if (_packageId == '2') return AppConstants.tkpJsonPath2;
    if (_packageId == '3') return AppConstants.tkpJsonPath3;
    return AppConstants.tkpJsonPath;
  }

  Future<List<Question>> loadAllQuestions() async {
    // Return cached data if valid
    if (_isCacheValid) {
      return _memoryCache!;
    }

    try {
      // Load secara eksplisit — biar error muncul jelas
      final twkPath = _twkPath();
      final tiuPath = _tiuPath();
      final tkpPath = _tkpPath();

      final twkFuture = _loadFromAsset(twkPath);
      final tiuFuture = _loadFromAsset(tiuPath);
      final tkpFuture = _loadFromAsset(tkpPath);

      final twkResults = await twkFuture;
      final tiuResults = await tiuFuture;
      final tkpResults = await tkpFuture;

      final allQuestions = <Question>[
        ...twkResults,
        ...tiuResults,
        ...tkpResults,
      ];

      // Update cache
      _memoryCache = allQuestions;
      _cacheTimestamp = DateTime.now();
      _cachedPackageId = _packageId;

      return allQuestions;
    } catch (e) {
      rethrow;
    }
  }

  Future<List<Question>> loadByCategory(String category) async {
    // Share cache from loadAllQuestions, filter by category
    final all = await loadAllQuestions();

    switch (category) {
      case 'TWK':
        return all.where((q) => q.category == 'TWK').toList();
      case 'TIU':
        return all.where((q) => q.category == 'TIU').toList();
      case 'TKP':
        return all.where((q) => q.category == 'TKP').toList();
      default:
        return all;
    }
  }

  Future<List<Question>> loadBySubcategory(String subcategory) async {
    final all = await loadAllQuestions();
    return all.where((q) => q.subcategory == subcategory).toList();
  }

  Future<List<Question>> loadPracticeQuestions({
    String? category,
    String? subcategory,
  }) async {
    // TUGAS 2: Ambil data dari SEMUA paket (1, 2, 3)
    final packages = ['1', '2', '3'];
    final originalPackage = _packageId; // simpan state awal

    try {
      // Loop tiap paket, load data, lalu gabungkan dengan `expand`
      final allFutures = packages.map((pkg) async {
        _packageId = pkg;
        if (category != null && (category == 'TWK' || category == 'TIU' || category == 'TKP')) {
          return await loadByCategory(category);
        } else {
          return await loadAllQuestions();
        }
      });

      // Tunggu semua proses selesai lalu gabungkan (flatten)
      final results = await Future.wait(allFutures);
      List<Question> questions = results.expand((list) => list).toList();

      // Filter by subcategory (case-insensitive, trimmed)
      if (subcategory != null && subcategory.isNotEmpty && subcategory != 'Semua') {
        final normalized = subcategory.toLowerCase().trim();
        questions = questions.where((q) => q.subcategory.toLowerCase().trim() == normalized).toList();
      }

      // Acak urutan — load semua soal yang ada, jangan potong
      questions.shuffle();
      return questions;
    } finally {
      // Pastikan state package ID dikembalikan ke semula walau error
      _packageId = originalPackage;
    }
  }

  Future<List<Question>> _loadFromAsset(String path) async {
    try {
      final jsonString = await rootBundle.loadString(path);
      // Parse JSON di background isolate — tidak memblokir UI thread
      final questions = await compute(_parseJsonInBackground, jsonString);
      return questions;
    } catch (e) {
      // Kembalikan array kosong — jangan throw, biar loadAllQuestions yang tangani
      return [];
    }
  }
}