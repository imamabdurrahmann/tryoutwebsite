import 'package:flutter/foundation.dart';
import 'package:hive_flutter/hive_flutter.dart';
import '../models/question.dart';
import '../models/tryout_session.dart';
import '../models/user_settings.dart';

class HiveSource {
  static const String questionsBox = 'questions';
  static const String sessionsBox = 'sessions';
  static const String settingsBox = 'settings';

  static Future<void> init() async {
    await Hive.initFlutter();

    Hive.registerAdapter(QuestionAdapter());
    Hive.registerAdapter(TryoutSessionAdapter());
    Hive.registerAdapter(UserSettingsAdapter());

    await Hive.openBox<Question>(questionsBox);
    await Hive.openBox<TryoutSession>(sessionsBox);
    await Hive.openBox<UserSettings>(settingsBox);

    // Clear stale questions cache — soal selalu dimuat fresh dari JSON assets
    await Hive.box<Question>(questionsBox).clear();
  }

  // ====== Questions ======
  Box<Question> get _questionsBox => Hive.box<Question>(questionsBox);

  Future<void> saveQuestions(List<Question> questions) async {
    await _questionsBox.clear();
    for (final q in questions) {
      await _questionsBox.put(q.questionId, q);
    }
  }

  List<Question> getAllQuestions() {
    return _questionsBox.values.toList();
  }

  List<Question> getQuestionsByCategory(String category) {
    return _questionsBox.values
        .where((q) => q.category == category)
        .toList();
  }

  List<Question> getQuestionsBySubcategory(String subcategory) {
    return _questionsBox.values
        .where((q) => q.subcategory == subcategory)
        .toList();
  }

  Future<void> clearQuestions() async {
    await _questionsBox.clear();
  }

  // ====== Tryout Sessions ======
  Box<TryoutSession> get _sessionsBox => Hive.box<TryoutSession>(sessionsBox);

  Future<void> saveSession(TryoutSession session) async {
    debugPrint('DEBUG: Saving session ${session.sessionId}');
    await _sessionsBox.put(session.sessionId, session);
    debugPrint('DEBUG: Session saved. Total sessions: ${_sessionsBox.length}');
  }

  List<TryoutSession> getAllSessions() {
    final sessions = _sessionsBox.values.toList();
    sessions.sort((a, b) => b.startTime.compareTo(a.startTime));
    return sessions;
  }

  TryoutSession? getSessionById(String sessionId) {
    return _sessionsBox.get(sessionId);
  }

  List<TryoutSession> getSessionsByPackageType(String type) {
    return _sessionsBox.values
        .where((s) => s.packageType == type)
        .toList()
      ..sort((a, b) => b.startTime.compareTo(a.startTime));
  }

  int getSessionCount() {
    return _sessionsBox.length;
  }

  List<TryoutSession> getRecentSessions({int limit = 10}) {
    final sessions = getAllSessions();
    return sessions.take(limit).toList();
  }

  Future<void> deleteSession(String sessionId) async {
    await _sessionsBox.delete(sessionId);
  }

  // ====== User Settings ======
  Box<UserSettings> get _settingsBox => Hive.box<UserSettings>(settingsBox);

  UserSettings getUserSettings() {
    final settings = _settingsBox.get('default');
    if (settings != null) return settings;

    final defaultSettings = UserSettings.createDefault();
    _settingsBox.put('default', defaultSettings);
    return defaultSettings;
  }

  Future<void> saveUserSettings(UserSettings settings) async {
    await _settingsBox.put('default', settings);
  }
}
