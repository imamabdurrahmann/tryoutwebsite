import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';

/// Service untuk auto-save dan resume tryout progress.
/// Menyimpan data ke SharedPreferences agar ringan dan tidak perlu Hive adapter baru.
class AutoSaveService {
  static const String _key = 'autosave_tryout';

  /// Simpan state tryout saat ini
  static Future<void> save({
    required String sessionId,
    required String packageType,
    required List<String> questionIds,
    required int currentIndex,
    required Map<String, String> answers,
    required Set<String> flaggedQuestions,
    required int remainingSeconds,
    required bool isPractice,
    bool isCatRealMode = false,
  }) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final data = {
        'sessionId': sessionId,
        'packageType': packageType,
        'questionIds': questionIds,
        'currentIndex': currentIndex,
        'answers': answers,
        'flaggedQuestions': flaggedQuestions.toList(),
        'remainingSeconds': remainingSeconds,
        'isPractice': isPractice,
        'isCatRealMode': isCatRealMode,
        'savedAt': DateTime.now().toIso8601String(),
      };
      await prefs.setString(_key, jsonEncode(data));
    } catch (e) {
      debugPrint('AutoSave error: $e');
    }
  }

  /// Ambil data tryout yang tersimpan (null jika tidak ada)
  static Future<Map<String, dynamic>?> load() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final raw = prefs.getString(_key);
      if (raw == null) return null;

      final data = jsonDecode(raw) as Map<String, dynamic>;

      // Expired setelah 24 jam
      final savedAt = DateTime.tryParse(data['savedAt'] ?? '');
      if (savedAt != null &&
          DateTime.now().difference(savedAt).inHours > 24) {
        await clear();
        return null;
      }

      return data;
    } catch (e) {
      debugPrint('AutoSave load error: $e');
      return null;
    }
  }

  /// Hapus data auto-save (setelah tryout selesai)
  static Future<void> clear() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove(_key);
  }

  /// Cek apakah ada data tersimpan
  static Future<bool> hasSavedData() async {
    final data = await load();
    return data != null;
  }
}
