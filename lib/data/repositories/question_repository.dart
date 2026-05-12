import 'package:shared_preferences/shared_preferences.dart';
import '../../core/constants/app_constants.dart';
import '../models/question.dart';
import '../sources/local_question_source.dart';
import '../sources/hive_source.dart';
import '../sources/remote_question_source.dart';

class QuestionRepository {
  final LocalQuestionSource _localSource = LocalQuestionSource();
  final HiveSource _hiveSource = HiveSource();
  final RemoteQuestionSource _remoteSource = RemoteQuestionSource();

  /// Cache per paket — Paket 1 dan Paket 2 punya cache sendiri-sendiri.
  final Map<String, List<Question>> _cacheByPackage = {};
  String _currentPackage = '1';

  /// Set active package: '1', '2', atau '3'. Clears cache if package changes.
  void setPackage(String packageId) {
    final id = (packageId == '2' || packageId == '3') ? packageId : '1';
    if (_currentPackage != id) {
      _currentPackage = id;
      LocalQuestionSource.setPackage(id);
      _cacheByPackage.clear();
    }
  }

  String get currentPackage => _currentPackage;

  Future<List<Question>> getAllQuestions() async {
    // ✅ FIX: Langsung baca dari JSON file. Tidak pernah pakai Hive cache
    // karena Hive box menyimpan semua paket campur-campur (Paket 1 + 2) dalam satu box.
    final questions = await _localSource.loadAllQuestions();
    _cacheByPackage[_currentPackage] = questions;
    return questions;
  }

  Future<List<Question>> getQuestionsByCategory(String category) async {
    // ✅ FIX: Langsung baca dari JSON file yang sesuai paket.
    // Bypass Hive cache yang mencampur semua paket dalam satu box.
    final questions = await _localSource.loadByCategory(category);
    _cacheByPackage[_currentPackage] = questions;
    return questions;
  }

  Future<List<Question>> getQuestionsBySubcategory(String subcategory) async {
    final all = await getAllQuestions();
    return all.where((q) => q.subcategory == subcategory).toList();
  }

  Future<List<Question>> getPracticeQuestions({
    String? category,
    String? subcategory,
  }) async {
    return _localSource.loadPracticeQuestions(
      category: category,
      subcategory: subcategory,
    );
  }

  Future<void> checkAndUpdateQuestions() async {
    try {
      final remoteVersion = await _remoteSource.checkVersion();
      if (remoteVersion == null) return;

      final prefs = await SharedPreferences.getInstance();
      final localVersion = prefs.getString(AppConstants.prefQuestionsVersion);

      if (remoteVersion != localVersion) {
        final newQuestions = await _remoteSource.downloadQuestions();
        if (newQuestions.isNotEmpty) {
          await _hiveSource.saveQuestions(newQuestions);
          _cacheByPackage.clear();
          await prefs.setString(AppConstants.prefQuestionsVersion, remoteVersion);
        }
      }
    } catch (_) {
      // Offline - skip update
    }
  }

  void clearCache() {
    _cacheByPackage.clear();
    _currentPackage = '1';
    LocalQuestionSource.setPackage('1');
  }
}
