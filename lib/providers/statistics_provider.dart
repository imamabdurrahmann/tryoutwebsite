import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../data/models/tryout_session.dart';
import '../data/repositories/result_repository.dart';

/// Data class for subcategory accuracy statistics
class SubcategoryStat {
  final String name;
  final String category; // TWK, TIU, TKP
  final int correct;
  final int total;
  final double accuracy;

  const SubcategoryStat({
    required this.name,
    required this.category,
    required this.correct,
    required this.total,
    required this.accuracy,
  });

  String get displayName => name.isEmpty ? 'Lainnya' : name;
}

/// Data class for overall statistics
class OverallStats {
  final int totalSessions;
  final int passedSessions;
  final double averageScore;
  final int bestScore;
  final double overallAccuracy;
  final int totalQuestionsAnswered;
  final int totalCorrect;

  const OverallStats({
    required this.totalSessions,
    required this.passedSessions,
    required this.averageScore,
    required this.bestScore,
    required this.overallAccuracy,
    required this.totalQuestionsAnswered,
    required this.totalCorrect,
  });
}

/// Data class for category accuracy
class CategoryAccuracy {
  final String category;
  final double accuracy;
  final int correct;
  final int total;
  final int passingGrade;
  final double averageScore;

  const CategoryAccuracy({
    required this.category,
    required this.accuracy,
    required this.correct,
    required this.total,
    required this.passingGrade,
    required this.averageScore,
  });
}

/// Data class for improvement trend
class TrendPoint {
  final DateTime date;
  final int sessionIndex;
  final double totalScore;
  final double twkScore;
  final double tiuScore;
  final double tkpScore;
  final bool passed;

  const TrendPoint({
    required this.date,
    required this.sessionIndex,
    required this.totalScore,
    required this.twkScore,
    required this.tiuScore,
    required this.tkpScore,
    required this.passed,
  });
}

/// State for statistics
class StatisticsState {
  final List<TryoutSession> sessions;
  final OverallStats overallStats;
  final List<CategoryAccuracy> categoryAccuracy;
  final List<SubcategoryStat> weakAreas;
  final List<SubcategoryStat> strongAreas;
  final List<TrendPoint> trendData;
  final bool isLoading;
  final String? error;

  const StatisticsState({
    required this.sessions,
    required this.overallStats,
    required this.categoryAccuracy,
    required this.weakAreas,
    required this.strongAreas,
    required this.trendData,
    this.isLoading = false,
    this.error,
  });

  factory StatisticsState.empty() {
    return StatisticsState(
      sessions: [],
      overallStats: const OverallStats(
        totalSessions: 0,
        passedSessions: 0,
        averageScore: 0,
        bestScore: 0,
        overallAccuracy: 0,
        totalQuestionsAnswered: 0,
        totalCorrect: 0,
      ),
      categoryAccuracy: [],
      weakAreas: [],
      strongAreas: [],
      trendData: [],
      isLoading: true,
    );
  }
}

/// Statistics Provider notifier
class StatisticsNotifier extends StateNotifier<StatisticsState> {
  final ResultRepository _resultRepository;

  StatisticsNotifier(this._resultRepository) : super(StatisticsState.empty()) {
    loadStatistics();
  }

  Future<void> loadStatistics() async {
    state = StatisticsState(
      sessions: state.sessions,
      overallStats: state.overallStats,
      categoryAccuracy: state.categoryAccuracy,
      weakAreas: state.weakAreas,
      strongAreas: state.strongAreas,
      trendData: state.trendData,
      isLoading: true,
      error: null,
    );

    try {
      final sessions = _resultRepository.getAllSessions();

      if (sessions.isEmpty) {
        state = StatisticsState(
          sessions: [],
          overallStats: const OverallStats(
            totalSessions: 0,
            passedSessions: 0,
            averageScore: 0,
            bestScore: 0,
            overallAccuracy: 0,
            totalQuestionsAnswered: 0,
            totalCorrect: 0,
          ),
          categoryAccuracy: [],
          weakAreas: [],
          strongAreas: [],
          trendData: [],
          isLoading: false,
        );
        return;
      }

      // Calculate all statistics
      final overallStats = _calculateOverallStats(sessions);
      final categoryAccuracy = _calculateCategoryAccuracy(sessions);
      final weakAreas = _calculateWeakAreas(sessions);
      final strongAreas = _calculateStrongAreas(sessions);
      final trendData = _calculateTrendData(sessions);

      state = StatisticsState(
        sessions: sessions,
        overallStats: overallStats,
        categoryAccuracy: categoryAccuracy,
        weakAreas: weakAreas,
        strongAreas: strongAreas,
        trendData: trendData,
        isLoading: false,
      );
    } catch (e) {
      state = StatisticsState(
        sessions: [],
        overallStats: state.overallStats,
        categoryAccuracy: state.categoryAccuracy,
        weakAreas: state.weakAreas,
        strongAreas: state.strongAreas,
        trendData: state.trendData,
        isLoading: false,
        error: e.toString(),
      );
    }
  }

  /// Get overall accuracy percentage
  double getOverallAccuracy() {
    return state.overallStats.overallAccuracy;
  }

  /// Get accuracy by category (TWK, TIU, TKP)
  List<CategoryAccuracy> getAccuracyByCategory() {
    return state.categoryAccuracy;
  }

  /// Get weak areas (subcategories with lowest accuracy)
  List<SubcategoryStat> getWeakAreas({int limit = 5}) {
    return state.weakAreas.take(limit).toList();
  }

  /// Get strong areas (subcategories with highest accuracy)
  List<SubcategoryStat> getStrongAreas({int limit = 5}) {
    return state.strongAreas.take(limit).toList();
  }

  /// Get improvement trend comparing recent vs older sessions
  Map<String, dynamic> getImprovementTrend() {
    if (state.trendData.length < 2) {
      return {'hasTrend': false, 'improving': false, 'change': 0};
    }

    final recent = state.trendData.last;
    final older = state.trendData[state.trendData.length - 2];

    final scoreChange = recent.totalScore - older.totalScore;
    final twkChange = recent.twkScore - older.twkScore;
    final tiuChange = recent.tiuScore - older.tiuScore;
    final tkpChange = recent.tkpScore - older.tkpScore;

    return {
      'hasTrend': true,
      'improving': scoreChange > 0,
      'scoreChange': scoreChange,
      'twkChange': twkChange,
      'tiuChange': tiuChange,
      'tkpChange': tkpChange,
      'recentScore': recent.totalScore,
      'olderScore': older.totalScore,
    };
  }

  OverallStats _calculateOverallStats(List<TryoutSession> sessions) {
    final totalSessions = sessions.length;
    final passedSessions = sessions.where((s) => s.overallPassed).length;

    final totalScores = sessions.fold<int>(0, (sum, s) => sum + s.totalScore);
    final averageScore = totalSessions > 0 ? totalScores / totalSessions : 0.0;

    final bestScore = sessions.isEmpty
        ? 0
        : sessions.map((s) => s.totalScore).reduce((a, b) => a > b ? a : b);

    // Calculate overall accuracy based on correct answers
    int totalCorrect = 0;
    int totalQuestions = 0;
    for (final s in sessions) {
      totalCorrect += s.twkCorrect + s.tiuCorrect;
      // TKP is scored differently - count as correct if answered
      totalCorrect += s.tkpAnswered;
      totalQuestions += s.twkQuestionCount + s.tiuQuestionCount + s.tkpQuestionCount;
    }

    final overallAccuracy = totalQuestions > 0
        ? (totalCorrect / totalQuestions) * 100
        : 0.0;

    return OverallStats(
      totalSessions: totalSessions,
      passedSessions: passedSessions,
      averageScore: averageScore,
      bestScore: bestScore,
      overallAccuracy: overallAccuracy,
      totalQuestionsAnswered: totalQuestions,
      totalCorrect: totalCorrect,
    );
  }

  List<CategoryAccuracy> _calculateCategoryAccuracy(List<TryoutSession> sessions) {
    final List<CategoryAccuracy> result = [];

    // TWK
    final twkSessions = sessions.where((s) => s.twkQuestionCount > 0).toList();
    if (twkSessions.isNotEmpty) {
      final totalCorrect = twkSessions.fold<int>(0, (sum, s) => sum + s.twkCorrect);
      final totalQuestions = twkSessions.fold<int>(0, (sum, s) => sum + s.twkQuestionCount);
      final totalScore = twkSessions.fold<int>(0, (sum, s) => sum + s.twkScore);
      final avgScore = totalScore / twkSessions.length;

      result.add(CategoryAccuracy(
        category: 'TWK',
        accuracy: totalQuestions > 0 ? (totalCorrect / totalQuestions) * 100 : 0,
        correct: totalCorrect,
        total: totalQuestions,
        passingGrade: 65,
        averageScore: avgScore,
      ));
    }

    // TIU
    final tiuSessions = sessions.where((s) => s.tiuQuestionCount > 0).toList();
    if (tiuSessions.isNotEmpty) {
      final totalCorrect = tiuSessions.fold<int>(0, (sum, s) => sum + s.tiuCorrect);
      final totalQuestions = tiuSessions.fold<int>(0, (sum, s) => sum + s.tiuQuestionCount);
      final totalScore = tiuSessions.fold<int>(0, (sum, s) => sum + s.tiuScore);
      final avgScore = totalScore / tiuSessions.length;

      result.add(CategoryAccuracy(
        category: 'TIU',
        accuracy: totalQuestions > 0 ? (totalCorrect / totalQuestions) * 100 : 0,
        correct: totalCorrect,
        total: totalQuestions,
        passingGrade: 80,
        averageScore: avgScore,
      ));
    }

    // TKP
    final tkpSessions = sessions.where((s) => s.tkpQuestionCount > 0).toList();
    if (tkpSessions.isNotEmpty) {
      // TKP: count answered as "correct" for accuracy purposes
      final totalAnswered = tkpSessions.fold<int>(0, (sum, s) => sum + s.tkpAnswered);
      final totalQuestions = tkpSessions.fold<int>(0, (sum, s) => sum + s.tkpQuestionCount);
      final totalScore = tkpSessions.fold<int>(0, (sum, s) => sum + s.tkpScore);
      final avgScore = totalScore / tkpSessions.length;

      result.add(CategoryAccuracy(
        category: 'TKP',
        accuracy: totalQuestions > 0 ? (totalAnswered / totalQuestions) * 100 : 0,
        correct: totalAnswered,
        total: totalQuestions,
        passingGrade: 166,
        averageScore: avgScore,
      ));
    }

    return result;
  }

  List<SubcategoryStat> _calculateWeakAreas(List<TryoutSession> sessions) {
    // Since sessions don't store subcategory data, we use category-level data
    // and create derived weak area indicators
    final List<SubcategoryStat> weakAreas = [];

    for (final cat in state.categoryAccuracy) {
      // If accuracy is below 70%, consider as weak area
      if (cat.accuracy < 70) {
        weakAreas.add(SubcategoryStat(
          name: cat.category,
          category: cat.category,
          correct: cat.correct,
          total: cat.total,
          accuracy: cat.accuracy,
        ));
      }
    }

    // Sort by accuracy (lowest first)
    weakAreas.sort((a, b) => a.accuracy.compareTo(b.accuracy));
    return weakAreas;
  }

  List<SubcategoryStat> _calculateStrongAreas(List<TryoutSession> sessions) {
    final List<SubcategoryStat> strongAreas = [];

    for (final cat in state.categoryAccuracy) {
      // If accuracy is above 70%, consider as strong area
      if (cat.accuracy >= 70) {
        strongAreas.add(SubcategoryStat(
          name: cat.category,
          category: cat.category,
          correct: cat.correct,
          total: cat.total,
          accuracy: cat.accuracy,
        ));
      }
    }

    // Sort by accuracy (highest first)
    strongAreas.sort((a, b) => b.accuracy.compareTo(a.accuracy));
    return strongAreas;
  }

  List<TrendPoint> _calculateTrendData(List<TryoutSession> sessions) {
    // Sort by date ascending for trend
    final sorted = List<TryoutSession>.from(sessions)
      ..sort((a, b) => a.startTime.compareTo(b.startTime));

    return sorted.asMap().entries.map((entry) {
      final index = entry.key;
      final session = entry.value;
      return TrendPoint(
        date: session.startTime,
        sessionIndex: index,
        totalScore: session.totalScore.toDouble(),
        twkScore: session.twkScore.toDouble(),
        tiuScore: session.tiuScore.toDouble(),
        tkpScore: session.tkpScore.toDouble(),
        passed: session.overallPassed,
      );
    }).toList();
  }
}

// Provider
final statisticsProvider = StateNotifierProvider<StatisticsNotifier, StatisticsState>((ref) {
  return StatisticsNotifier(ResultRepository());
});

// Convenience providers
final statisticsOverallStatsProvider = Provider<OverallStats>((ref) {
  return ref.watch(statisticsProvider).overallStats;
});

final statisticsCategoryAccuracyProvider = Provider<List<CategoryAccuracy>>((ref) {
  return ref.watch(statisticsProvider).categoryAccuracy;
});

final statisticsWeakAreasProvider = Provider<List<SubcategoryStat>>((ref) {
  return ref.watch(statisticsProvider).weakAreas;
});

final statisticsStrongAreasProvider = Provider<List<SubcategoryStat>>((ref) {
  return ref.watch(statisticsProvider).strongAreas;
});

final statisticsTrendDataProvider = Provider<List<TrendPoint>>((ref) {
  return ref.watch(statisticsProvider).trendData;
});
