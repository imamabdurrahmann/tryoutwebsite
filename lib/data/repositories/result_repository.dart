import '../models/tryout_session.dart';
import '../sources/hive_source.dart';

class ResultRepository {
  final HiveSource _hiveSource = HiveSource();

  Future<void> saveSession(TryoutSession session) async {
    await _hiveSource.saveSession(session);
  }

  List<TryoutSession> getAllSessions() {
    return _hiveSource.getAllSessions();
  }

  TryoutSession? getSessionById(String sessionId) {
    return _hiveSource.getSessionById(sessionId);
  }

  List<TryoutSession> getSessionsByPackageType(String type) {
    return _hiveSource.getSessionsByPackageType(type);
  }

  List<TryoutSession> getRecentSessions({int limit = 10}) {
    return _hiveSource.getRecentSessions(limit: limit);
  }

  int getTotalSessionCount() {
    return _hiveSource.getSessionCount();
  }

  double getAverageScore() {
    final sessions = getAllSessions();
    if (sessions.isEmpty) return 0;

    final totalScore = sessions.fold<int>(
      0,
      (sum, s) => sum + s.totalScore,
    );
    return totalScore / sessions.length;
  }

  Map<String, double> getCategoryAccuracy() {
    final sessions = getAllSessions();
    if (sessions.isEmpty) {
      return {'TWK': 0, 'TIU': 0, 'TKP': 0};
    }

    double twkAvg = 0, tiuAvg = 0, tkpAvg = 0;
    for (final s in sessions) {
      twkAvg += s.twkScore;
      tiuAvg += s.tiuScore;
      tkpAvg += s.tkpScore;
    }

    final count = sessions.length;
    return {
      'TWK': twkAvg / count,
      'TIU': tiuAvg / count,
      'TKP': tkpAvg / count,
    };
  }

  List<Map<String, dynamic>> getProgressData() {
    final sessions = getAllSessions();
    if (sessions.isEmpty) return [];

    return sessions.reversed.map((s) {
      return {
        'date': s.startTime,
        'totalScore': s.totalScore,
        'twkScore': s.twkScore,
        'tiuScore': s.tiuScore,
        'tkpScore': s.tkpScore,
        'overallPassed': s.overallPassed,
      };
    }).toList();
  }

  Future<void> deleteSession(String sessionId) async {
    await _hiveSource.deleteSession(sessionId);
  }

  /// Get sessions with pagination for lazy loading
  /// [limit] = jumlah item per page (default 20)
  /// [offset] = start index (default 0)
  List<TryoutSession> getSessionsPaginated({
    int limit = 20,
    int offset = 0,
  }) {
    final all = getAllSessions();
    if (offset >= all.length) return [];
    final end = (offset + limit).clamp(0, all.length);
    return all.sublist(offset, end);
  }

  /// Check if there's more data
  bool hasMoreSessions(int offset, {int limit = 20}) {
    return offset < getTotalSessionCount();
  }
}
