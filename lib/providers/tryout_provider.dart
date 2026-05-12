import 'dart:async';
import 'dart:convert';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../data/models/question.dart';
import '../data/models/tryout_session.dart';
import '../data/repositories/result_repository.dart';
import '../data/repositories/user_repository.dart';
import '../core/utils/score_calculator.dart';
import '../core/utils/auto_save_service.dart';
import '../core/models/package_metadata.dart';

final resultRepositoryProvider = Provider((ref) => ResultRepository());
final userRepositoryProvider = Provider((ref) => UserRepository());

// ====== Tryout Session State ======
class TryoutState {
  final String sessionId;
  final String packageType;
  final List<Question> questions;
  final int currentIndex;
  final Map<String, String> answers;
  final Set<String> flaggedQuestions;
  final Set<String> visitedQuestions;
  final int remainingSeconds;
  final bool isFinished;
  final bool isPaused;
  final bool isPractice;
  final bool showAnswerImmediately;
  final bool isCatRealMode;

  const TryoutState({
    required this.sessionId,
    required this.packageType,
    required this.questions,
    this.currentIndex = 0,
    this.answers = const {},
    this.flaggedQuestions = const {},
    this.visitedQuestions = const {},
    this.remainingSeconds = 0,
    this.isFinished = false,
    this.isPaused = false,
    this.isPractice = false,
    this.showAnswerImmediately = false,
    this.isCatRealMode = false,
  });

  Question? get currentQuestion =>
      questions.isNotEmpty && currentIndex < questions.length
          ? questions[currentIndex]
          : null;

  bool get canGoNext => currentIndex < questions.length - 1;
  bool get canGoPrev => currentIndex > 0;

  int get answeredCount => answers.length;
  int get totalCount => questions.length;
  double get progress => totalCount > 0 ? answeredCount / totalCount : 0;

  int get correctCount => questions.where((q) {
    final ans = answers[q.questionId];
    return ans == q.answer;
  }).length;

  int get wrongCount => questions.where((q) {
    final ans = answers[q.questionId];
    return ans != null && ans != q.answer && ans.isNotEmpty;
  }).length;

  int get unansweredCount => totalCount - answeredCount;

  TryoutState copyWith({
    String? sessionId,
    String? packageType,
    List<Question>? questions,
    int? currentIndex,
    Map<String, String>? answers,
    Set<String>? flaggedQuestions,
    Set<String>? visitedQuestions,
    int? remainingSeconds,
    bool? isFinished,
    bool? isPaused,
    bool? isPractice,
    bool? showAnswerImmediately,
    bool? isCatRealMode,
  }) {
    return TryoutState(
      sessionId: sessionId ?? this.sessionId,
      packageType: packageType ?? this.packageType,
      questions: questions ?? this.questions,
      currentIndex: currentIndex ?? this.currentIndex,
      answers: answers ?? this.answers,
      flaggedQuestions: flaggedQuestions ?? this.flaggedQuestions,
      visitedQuestions: visitedQuestions ?? this.visitedQuestions,
      remainingSeconds: remainingSeconds ?? this.remainingSeconds,
      isFinished: isFinished ?? this.isFinished,
      isPaused: isPaused ?? this.isPaused,
      isPractice: isPractice ?? this.isPractice,
      showAnswerImmediately: showAnswerImmediately ?? this.showAnswerImmediately,
      isCatRealMode: isCatRealMode ?? this.isCatRealMode,
    );
  }
}

class TryoutNotifier extends StateNotifier<TryoutState?> {
  Timer? _timer;
  final Ref _ref;

  TryoutNotifier(this._ref) : super(null);

  void startTryout({
    required List<Question> questions,
    required String packageType,
    bool isPractice = false,
    bool isCatRealMode = false,
  }) {
    _timer?.cancel();

    final duration = _getDuration(packageType, isPractice);
    final sessionId = DateTime.now().millisecondsSinceEpoch.toString();

    // Mark first question as visited on start
    final firstQuestionId = questions.isNotEmpty ? questions.first.questionId : '';
    final initialVisited = firstQuestionId.isNotEmpty ? {firstQuestionId} : <String>{};

    state = TryoutState(
      sessionId: sessionId,
      packageType: packageType,
      questions: questions,
      remainingSeconds: duration,
      isPractice: isPractice,
      showAnswerImmediately: isPractice,
      isCatRealMode: isCatRealMode,
      visitedQuestions: initialVisited,
    );

    if (!isPractice) {
      _startTimer();
    }
  }

  int _getDuration(String packageType, bool isPractice) {
    if (isPractice) return 0;
    final meta = PackageMetadataRepository.get(packageType);
    return meta.durationMinutes * 60;
  }

  void _startTimer() {
    _timer = Timer.periodic(const Duration(seconds: 1), (_) {
      if (state == null || state!.isFinished || state!.isPaused) return;

      // Never run timer in practice mode — _getDuration returns sentinel for practice
      if (state!.isPractice) return;

      final remaining = state!.remainingSeconds - 1;
      if (remaining <= 0) {
        _timer?.cancel();
        finishTryout();
      } else {
        state = state!.copyWith(remainingSeconds: remaining);
      }
    });
  }

  void selectAnswer(String answer) {
    if (state == null || state!.isFinished) return;

    final q = state!.currentQuestion;
    if (q == null) return;

    final newAnswers = Map<String, String>.from(state!.answers);
    newAnswers[q.questionId] = answer;

    state = state!.copyWith(answers: newAnswers);
    _autoSave();
  }

  void visitQuestion(String questionId) {
    if (state == null || state!.isFinished) return;
    if (state!.visitedQuestions.contains(questionId)) return;

    final newVisited = Set<String>.from(state!.visitedQuestions)..add(questionId);
    state = state!.copyWith(visitedQuestions: newVisited);
  }

  void toggleFlag() {
    if (state == null || state!.isFinished) return;

    final q = state!.currentQuestion;
    if (q == null) return;

    final newFlagged = Set<String>.from(state!.flaggedQuestions);
    if (newFlagged.contains(q.questionId)) {
      newFlagged.remove(q.questionId);
    } else {
      newFlagged.add(q.questionId);
    }

    state = state!.copyWith(flaggedQuestions: newFlagged);
    _autoSave();
  }

  void goToQuestion(int index) {
    if (state == null || state!.isFinished) return;
    if (index < 0 || index >= state!.questions.length) return;

    final q = state!.questions[index];
    visitQuestion(q.questionId);
    state = state!.copyWith(currentIndex: index);
    _autoSave();
  }

  void nextQuestion() {
    if (state == null || state!.isFinished) return;
    if (state!.canGoNext) {
      final nextIndex = state!.currentIndex + 1;
      final nextQ = state!.questions[nextIndex];
      visitQuestion(nextQ.questionId);
      state = state!.copyWith(currentIndex: nextIndex);
    }
  }

  void prevQuestion() {
    if (state == null || state!.isFinished) return;
    if (state!.canGoPrev) {
      final prevIndex = state!.currentIndex - 1;
      final prevQ = state!.questions[prevIndex];
      visitQuestion(prevQ.questionId);
      state = state!.copyWith(currentIndex: prevIndex);
    }
  }

  /// Start practice mode: set questions directly (already filtered/shuffled)
  void startPracticeWithQuestions(List<Question> questions, {bool isCatRealMode = false}) {
    _timer?.cancel();
    state = TryoutState(
      sessionId: DateTime.now().millisecondsSinceEpoch.toString(),
      packageType: 'PRACTICE',
      questions: questions,
      remainingSeconds: 0,
      isPractice: true,
      showAnswerImmediately: false, // TUGAS 3: Kunci jawaban dimatikan di awal
      isCatRealMode: isCatRealMode,
      visitedQuestions: questions.isNotEmpty ? {questions.first.questionId} : {},
    );
  }

  void pauseTryout() {
    if (state == null || state!.isFinished) return;
    _timer?.cancel();
    state = state!.copyWith(isPaused: true);
  }

  void resumeTryout() {
    if (state == null || state!.isFinished) return;
    state = state!.copyWith(isPaused: false);
    if (!state!.isPractice) _startTimer();
  }

  Future<TryoutSession> finishTryout() async {
    if (state == null) throw Exception('No active tryout');

    _timer?.cancel();

    state = state!.copyWith(isFinished: true);

    // Clear auto-save on finish
    await AutoSaveService.clear();

    final scoreResult = ScoreCalculator.calculate(
      state!.questions,
      state!.answers,
      state!.packageType,
    );

    final session = TryoutSession.create(
      sessionId: state!.sessionId,
      packageType: state!.packageType,
      startTime: DateTime.now().subtract(
        Duration(seconds: _getDuration(state!.packageType, state!.isPractice) - state!.remainingSeconds),
      ),
      endTime: DateTime.now(),
      durationSeconds: _getDuration(state!.packageType, state!.isPractice) - state!.remainingSeconds,
      answersJson: jsonEncode(state!.answers),
      flaggedQuestions: state!.flaggedQuestions.toList(),
      totalScore: scoreResult.totalScore,
      twkScore: scoreResult.twkScaled,
      tiuScore: scoreResult.tiuScaled,
      tkpScore: scoreResult.tkpScore,
      twkPassed: scoreResult.twkPassed,
      tiuPassed: scoreResult.tiuPassed,
      tkpPassed: scoreResult.tkpPassed,
      overallPassed: scoreResult.overallPassed,
      twkCorrect: scoreResult.twkCorrect,
      tiuCorrect: scoreResult.tiuCorrect,
      tkpAnswered: scoreResult.tkpAnswered,
      twkWrong: scoreResult.twkWrong,
      tiuWrong: scoreResult.tiuWrong,
      twkUnanswered: scoreResult.twkUnanswered,
      tiuUnanswered: scoreResult.tiuUnanswered,
      tkpUnanswered: scoreResult.tkpUnanswered,
      twkQuestionCount: scoreResult.twkQuestionCount,
      tiuQuestionCount: scoreResult.tiuQuestionCount,
      tkpQuestionCount: scoreResult.tkpQuestionCount,
      isCatRealMode: state!.isCatRealMode,
    );

    final resultRepo = _ref.read(resultRepositoryProvider);
    await resultRepo.saveSession(session);

    final userRepo = _ref.read(userRepositoryProvider);
    await userRepo.incrementSessionCount();

    // Refresh sessions list
    _ref.read(sessionsNotifierProvider.notifier).refresh();

    return session;
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  /// Auto-save current tryout state
  void _autoSave() {
    if (state == null || state!.isFinished) return;
    AutoSaveService.save(
      sessionId: state!.sessionId,
      packageType: state!.packageType,
      questionIds: state!.questions.map((q) => q.questionId).toList(),
      currentIndex: state!.currentIndex,
      answers: state!.answers,
      flaggedQuestions: state!.flaggedQuestions,
      remainingSeconds: state!.remainingSeconds,
      isPractice: state!.isPractice,
      isCatRealMode: state!.isCatRealMode,
    );
  }

  /// Resume tryout dari data auto-save
  Future<bool> resumeFromAutoSave(List<Question> allQuestions) async {
    final data = await AutoSaveService.load();
    if (data == null) return false;

    try {
      final questionIds = List<String>.from(data['questionIds'] ?? []);
      final questions = <Question>[];
      for (final id in questionIds) {
        final q = allQuestions.where((q) => q.questionId == id).firstOrNull;
        if (q != null) questions.add(q);
      }

      if (questions.isEmpty) {
        await AutoSaveService.clear();
        return false;
      }

      final answers = Map<String, String>.from(data['answers'] ?? {});
      final flagged = Set<String>.from(List<String>.from(data['flaggedQuestions'] ?? []));
      final visited = Set<String>.from(questionIds); // semua sudah dikunjungi

      _timer?.cancel();
      state = TryoutState(
        sessionId: data['sessionId'] ?? DateTime.now().millisecondsSinceEpoch.toString(),
        packageType: data['packageType'] ?? 'FULL',
        questions: questions,
        currentIndex: data['currentIndex'] ?? 0,
        answers: answers,
        flaggedQuestions: flagged,
        visitedQuestions: visited,
        remainingSeconds: data['remainingSeconds'] ?? 0,
        isPractice: data['isPractice'] ?? false,
        showAnswerImmediately: data['isPractice'] ?? false,
        isCatRealMode: data['isCatRealMode'] ?? false,
      );

      if (!state!.isPractice && state!.remainingSeconds > 0) {
        _startTimer();
      }

      return true;
    } catch (e) {
      await AutoSaveService.clear();
      return false;
    }
  }

  /// Set CAT Real mode before starting tryout
  void setCatRealMode(bool isCatRealMode) {
    if (state == null) {
      // No active state, create one with just the mode flag
      // This will be overridden by startTryout or startPracticeWithQuestions
      state = TryoutState(
        sessionId: DateTime.now().millisecondsSinceEpoch.toString(),
        packageType: 'UNKNOWN',
        questions: [],
        isCatRealMode: isCatRealMode,
      );
    } else {
      state = state!.copyWith(isCatRealMode: isCatRealMode);
    }
  }
}

final tryoutProvider = StateNotifierProvider<TryoutNotifier, TryoutState?>((ref) {
  return TryoutNotifier(ref);
});

// ====== Session Detail Provider (Async) ======
final sessionDetailProvider = FutureProvider.family<TryoutSession?, String>((ref, sessionId) async {
  final repo = ref.watch(resultRepositoryProvider);
  return repo.getSessionById(sessionId);
});

// ====== All Sessions Provider (Async) ======
final allSessionsProvider = FutureProvider<List<TryoutSession>>((ref) async {
  final repo = ref.watch(resultRepositoryProvider);
  return repo.getAllSessions();
});

// ====== Sessions Notifier for Refreshing ======
class SessionsNotifier extends StateNotifier<AsyncValue<List<TryoutSession>>> {
  final Ref _ref;

  SessionsNotifier(this._ref) : super(const AsyncValue.loading()) {
    _load();
  }

  Future<void> _load() async {
    try {
      final repo = _ref.read(resultRepositoryProvider);
      final sessions = await Future.value(repo.getAllSessions());
      if (mounted) {
        state = AsyncValue.data(sessions);
      }
    } catch (e, st) {
      if (mounted) {
        state = AsyncValue.error(e, st);
      }
    }
  }

  Future<void> refresh() async {
    state = const AsyncValue.loading();
    await _load();
  }
}

final sessionsNotifierProvider = StateNotifierProvider<SessionsNotifier, AsyncValue<List<TryoutSession>>>((ref) {
  return SessionsNotifier(ref);
});

// ====== Progress Data Provider (Async) ======
final progressDataProvider = FutureProvider<List<Map<String, dynamic>>>((ref) async {
  final repo = ref.watch(resultRepositoryProvider);
  return repo.getProgressData();
});

// ====== Category Accuracy Provider (Async) ======
final categoryAccuracyProvider = FutureProvider<Map<String, double>>((ref) async {
  final repo = ref.watch(resultRepositoryProvider);
  return repo.getCategoryAccuracy();
});

// ====== Sessions Pagination Provider (for lazy loading) ======
/// Load sessions page by page
/// [page] = page number (0-indexed)
final sessionsPageProvider = FutureProvider.family<List<TryoutSession>, int>((ref, page) async {
  final repo = ref.watch(resultRepositoryProvider);
  const limit = 20;
  return repo.getSessionsPaginated(offset: page * limit, limit: limit);
});

/// Check if there's more data after a given offset
final hasMoreSessionsProvider = Provider.family<bool, int>((ref, offset) {
  final repo = ref.watch(resultRepositoryProvider);
  return repo.hasMoreSessions(offset, limit: 20);
});
