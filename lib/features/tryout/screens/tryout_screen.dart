import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import '../../../core/constants/app_constants.dart';
import '../../../core/models/package_metadata.dart';
import '../../../core/theme/app_theme.dart';
import '../../../data/models/question.dart';
import '../../../providers/questions_provider.dart';
import '../../../providers/tryout_provider.dart';
import '../widgets/question_card.dart';
import '../widgets/timer_widget.dart';
import '../widgets/navigation_bar.dart';

class TryoutScreen extends ConsumerStatefulWidget {
  final String packageType;

  const TryoutScreen({super.key, required this.packageType});

  @override
  ConsumerState<TryoutScreen> createState() => _TryoutScreenState();
}

class _TryoutScreenState extends ConsumerState<TryoutScreen> {
  bool _isLoading = true;
  bool _timeUpOverlayShown = false;
  final Set<int> _shownWarnings = {};
  final FocusNode _focusNode = FocusNode();

  @override
  void initState() {
    super.initState();
    _initializeTryout();
  }

  @override
  void dispose() {
    _focusNode.dispose();
    super.dispose();
  }

  void _handleKeyEvent(KeyEvent event) {
    if (event is! KeyDownEvent) return;
    final tryout = ref.read(tryoutProvider);
    if (tryout == null || tryout.isFinished) return;

    final key = event.logicalKey;
    // A-E: select answer
    if (key == LogicalKeyboardKey.keyA) ref.read(tryoutProvider.notifier).selectAnswer('A');
    if (key == LogicalKeyboardKey.keyB) ref.read(tryoutProvider.notifier).selectAnswer('B');
    if (key == LogicalKeyboardKey.keyC) ref.read(tryoutProvider.notifier).selectAnswer('C');
    if (key == LogicalKeyboardKey.keyD) ref.read(tryoutProvider.notifier).selectAnswer('D');
    if (key == LogicalKeyboardKey.keyE) ref.read(tryoutProvider.notifier).selectAnswer('E');
    // Arrow keys: navigation (CAT Real mode: only forward)
    if (key == LogicalKeyboardKey.arrowRight || key == LogicalKeyboardKey.arrowDown) {
      ref.read(tryoutProvider.notifier).nextQuestion();
    }
    // CAT Real mode: DISALLOW going back
    if (!tryout.isCatRealMode) {
      if (key == LogicalKeyboardKey.arrowLeft || key == LogicalKeyboardKey.arrowUp) {
        ref.read(tryoutProvider.notifier).prevQuestion();
      }
    }
    // F: flag
    if (key == LogicalKeyboardKey.keyF) ref.read(tryoutProvider.notifier).toggleFlag();
  }

  Future<void> _initializeTryout() async {
    // ✅ PRACTICE mode: State sudah di-set oleh PracticeScreen via startPracticeWithQuestions().
    // Cek apakah sudah ada questions di state. Jika ada, skip _loadQuestions().
    final existing = ref.read(tryoutProvider);
    if (existing != null && existing.packageType == 'PRACTICE' && existing.questions.isNotEmpty) {
      setState(() => _isLoading = false);
      return;
    }

    // Non-practice: load questions dari repo seperti biasa
    _loadQuestions();
  }

  Future<void> _loadQuestions() async {
    final repo = ref.read(questionRepositoryProvider);

    // Paket 1 vs Paket 2 vs Paket 3
    final pType = widget.packageType;
    final packageNum = AppConstants.extractPackageNumber(pType);
    repo.setPackage(packageNum);

    List<Question> questions;

    // Tangkap jenis tes berdasarkan packageId
    if (pType == 'FULL' || pType == 'FULL_2' || pType == 'FULL_3') {
      questions = await repo.getAllQuestions();
    } else if (pType == 'TWK_ONLY' || pType == 'TWK_ONLY_2' || pType == 'TWK_ONLY_3') {
      questions = await repo.getQuestionsByCategory(AppConstants.categoryTwk);
    } else if (pType == 'TIU_ONLY' || pType == 'TIU_ONLY_2' || pType == 'TIU_ONLY_3') {
      questions = await repo.getQuestionsByCategory(AppConstants.categoryTiu);
    } else if (pType == 'TKP_ONLY' || pType == 'TKP_ONLY_2' || pType == 'TKP_ONLY_3') {
      questions = await repo.getQuestionsByCategory(AppConstants.categoryTkp);
    } else {
      repo.setPackage('1');
      questions = await repo.getAllQuestions();
    }

    if (!mounted) return;

    // ✅ PRACTICE mode tidak punya timer, jawaban langsung tampil
    final isPractice = widget.packageType == 'PRACTICE';

    // Get isCatRealMode from existing state (set by preparation_screen)
    final existingState = ref.read(tryoutProvider);
    final isCatRealMode = existingState?.isCatRealMode ?? false;

    ref.read(tryoutProvider.notifier).startTryout(
      questions: questions,
      packageType: widget.packageType,
      isPractice: isPractice,
      isCatRealMode: isCatRealMode,
    );

    setState(() => _isLoading = false);
  }

  @override
  Widget build(BuildContext context) {
    final tryout = ref.watch(tryoutProvider);

    if (_isLoading || tryout == null) {
      return Scaffold(
        appBar: AppBar(title: const Text('Memuat...')),
        body: const Center(child: CircularProgressIndicator()),
      );
    }

    // Auto-submit when finished
    if (tryout.isFinished) {
      WidgetsBinding.instance.addPostFrameCallback((_) {
        context.go('/result/${tryout.sessionId}');
      });
    }

    // Time warning system — SnackBar thresholds
    if (!tryout.isPractice) {
      _checkTimeWarnings(tryout.remainingSeconds);
    }

    // "Waktu Habis!" overlay at 0 seconds — skip in practice mode
    if (tryout.remainingSeconds == 0 && !_timeUpOverlayShown && !tryout.isFinished && !tryout.isPractice) {
      _timeUpOverlayShown = true;
      WidgetsBinding.instance.addPostFrameCallback((_) {
        _showTimeUpOverlay(context);
      });
    }

    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, result) {
        if (!didPop) _showExitConfirmation(context);
      },
      child: KeyboardListener(
        focusNode: _focusNode,
        autofocus: true,
        onKeyEvent: _handleKeyEvent,
        child: Scaffold(
        appBar: AppBar(
          title: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  if (tryout.isCatRealMode)
                    Container(
                      margin: const EdgeInsets.only(right: 8),
                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                      decoration: BoxDecoration(
                        color: AppTheme.primaryRed,
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: const Text(
                        'CAT REAL',
                        style: TextStyle(
                          color: Colors.white,
                          fontSize: 10,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                  Expanded(child: Text(_getTitle(), style: const TextStyle(fontSize: 16))),
                ],
              ),
              Text(
                'Soal ${tryout.currentIndex + 1} dari ${tryout.totalCount} · ${tryout.answeredCount} terjawab',
                style: const TextStyle(fontSize: 11, fontWeight: FontWeight.normal),
              ),
            ],
          ),
          leading: IconButton(
            icon: const Icon(Icons.close),
            onPressed: () => _showExitConfirmation(context),
          ),
          actions: [
            if (!tryout.isPractice) ...[
              TimerWidget(remainingSeconds: tryout.remainingSeconds),
              const SizedBox(width: 8),
            ],
            IconButton(
              icon: Icon(
                tryout.flaggedQuestions.contains(
                        tryout.currentQuestion?.questionId)
                    ? Icons.flag
                    : Icons.flag_outlined,
                color: tryout.flaggedQuestions
                        .contains(tryout.currentQuestion?.questionId)
                    ? AppTheme.warningOrange
                    : null,
              ),
              onPressed: () {
                ref.read(tryoutProvider.notifier).toggleFlag();
              },
              tooltip: 'Tandai',
            ),
          ],
        ),
        body: SafeArea(
          child: Center(
            child: ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 900), // TUGAS 1: Max width 900
              child: Column(
                children: [
                  // Progress Bar
                  LinearProgressIndicator(
                    value: tryout.progress,
                    backgroundColor: Colors.grey.shade200,
                    valueColor: const AlwaysStoppedAnimation(AppTheme.primaryRed),
                  ),

                  // Question Content — Expanded + Scrollable
                  Expanded(
                    child: AnimatedSwitcher(
                      duration: const Duration(milliseconds: 300),
                      transitionBuilder: (Widget child, Animation<double> animation) {
                        return FadeTransition(
                          opacity: animation,
                          child: SlideTransition(
                            position: Tween<Offset>(
                              begin: const Offset(0.05, 0),
                              end: Offset.zero,
                            ).animate(CurvedAnimation(
                              parent: animation,
                              curve: Curves.easeOut,
                            )),
                            child: child,
                          ),
                        );
                      },
                      child: SingleChildScrollView(
                        key: ValueKey<int>(tryout.currentIndex),
                        padding: EdgeInsets.fromLTRB(
                          16,
                          16,
                          16,
                          _bottomPadding(context),
                        ),
                        child: QuestionCard(
                          question: tryout.currentQuestion!,
                          selectedAnswer: tryout.answers[tryout.currentQuestion!.questionId],
                          onAnswerSelected: (answer) {
                            ref.read(tryoutProvider.notifier).selectAnswer(answer);
                          },
                          showAnswer: tryout.showAnswerImmediately,
                          isPracticeMode: tryout.isPractice,
                        ),
                      ),
                    ),
                  ),

                  // Navigation Buttons (fixed above nav bar)
              Container(
                padding: EdgeInsets.fromLTRB(
                  16,
                  12,
                  16,
                  _calcBottomNavBarHeight(context),
                ),
                decoration: BoxDecoration(
                  color: Theme.of(context).cardColor,
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black.withAlpha(13),
                      blurRadius: 8,
                      offset: const Offset(0, -2),
                    ),
                  ],
                ),
                child: Row(
                  children: [
                    // Hide Previous button in CAT Real mode
                    if (tryout.canGoPrev && !tryout.isCatRealMode)
                      Expanded(
                        child: OutlinedButton.icon(
                          onPressed: () {
                            ref.read(tryoutProvider.notifier).prevQuestion();
                          },
                          icon: const Icon(Icons.arrow_back),
                          label: const Text('Sebelumnya'),
                        ),
                      )
                    else
                      const Spacer(),
                    const SizedBox(width: 8),
                    Expanded(
                      child: ElevatedButton.icon(
                        onPressed: () {
                          // CAT Real mode: must answer first
                          if (tryout.isCatRealMode) {
                            if (tryout.isCurrentQuestionAnswered && tryout.canGoNext) {
                              ref.read(tryoutProvider.notifier).nextQuestion();
                            } else if (!tryout.isCurrentQuestionAnswered) {
                              // Show warning that must answer first
                              ScaffoldMessenger.of(context).showSnackBar(
                                const SnackBar(
                                  content: Text('⚠️ Jawab dulu sebelum lanjut!'),
                                  duration: Duration(seconds: 2),
                                ),
                              );
                            } else {
                              // Last question, submit
                              _showSubmitConfirmation(context);
                            }
                          } else if (tryout.canGoNext) {
                            ref.read(tryoutProvider.notifier).nextQuestion();
                          } else if (tryout.isPractice) {
                            // ✅ Practice mode: konfirmasi dulu, lalu return ke home
                            _showPracticeExitConfirmation(context);
                          } else {
                            _showSubmitConfirmation(context);
                          }
                        },
                        icon: Icon(tryout.isCatRealMode
                            ? (tryout.isCurrentQuestionAnswered && tryout.canGoNext
                                ? Icons.arrow_forward
                                : (tryout.isCurrentQuestionAnswered ? Icons.check : Icons.lock))
                            : (tryout.canGoNext
                                ? Icons.arrow_forward
                                : Icons.check)),
                        label: Text(
                          tryout.isCatRealMode
                              ? (tryout.isCurrentQuestionAnswered
                                  ? (tryout.canGoNext ? 'Selanjutnya' : 'Selesai')
                                  : 'Jawab Dulu')
                              : (tryout.canGoNext ? 'Selanjutnya' : 'Selesai'),
                        ),
                        style: tryout.isCatRealMode && !tryout.isCurrentQuestionAnswered
                            ? ElevatedButton.styleFrom(
                                backgroundColor: Colors.grey,
                              )
                            : null,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
        ),
        ),
        // Bottom Navigation (Question Number Grid) via Scaffold's bottomNavigationBar
        bottomNavigationBar: RepaintBoundary(
          child: QuestionNavBar(
            totalQuestions: tryout.totalCount,
            currentIndex: tryout.currentIndex,
            answers: tryout.answers,
            flagged: tryout.flaggedQuestions,
            visited: tryout.visitedQuestions,
            questions: tryout.questions,
            onQuestionTap: tryout.isCatRealMode
                ? (_) {} // Disabled in CAT Real mode
                : (index) {
                    ref.read(tryoutProvider.notifier).goToQuestion(index);
                  },
            isCatRealMode: tryout.isCatRealMode,
          ),
        ),
      ),
      ),
    );
  }

  String _getTitle() {
    final meta = PackageMetadataRepository.get(widget.packageType);
    return '${meta.title} (${meta.subtitle})';
  }

  void _showExitConfirmation(BuildContext context) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Keluar dari Try Out?'),
        content: const Text(
          'Progres try out akan hilang jika kamu keluar sekarang.',
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Tetap Di Sini'),
          ),
          TextButton(
            onPressed: () {
              Navigator.pop(context);
              context.go('/home');
            },
            child: const Text('Keluar'),
          ),
        ],
      ),
    );
  }

  void _showPracticeExitConfirmation(BuildContext context) {
    // ✅ Practice mode: hanya konfirmasi, lalu return ke home (bukan ResultScreen)
    final tryout = ref.read(tryoutProvider);
    if (tryout == null) return;

    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        title: const Row(
          children: [
            Icon(Icons.school, color: AppTheme.primaryRed),
            SizedBox(width: 8),
            Text('Akhiri Latihan?'),
          ],
        ),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            _buildSummaryRow(
              'Total Soal',
              '${tryout.totalCount}',
              Colors.grey.shade700,
            ),
            const SizedBox(height: 6),
            _buildSummaryRow(
              'Sudah Dijawab',
              '${tryout.answeredCount}',
              AppTheme.catAnswered,
            ),
            const SizedBox(height: 6),
            _buildSummaryRow(
              'Belum Dijawab',
              '${tryout.unansweredCount}',
              tryout.unansweredCount > 0 ? AppTheme.catVisitedEmpty : Colors.grey,
            ),
            const SizedBox(height: 16),
            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: AppTheme.secondaryBlue.withAlpha(15),
                borderRadius: BorderRadius.circular(8),
                border: Border.all(color: AppTheme.secondaryBlue.withAlpha(40)),
              ),
              child: const Row(
                children: [
                  Icon(Icons.info_outline, color: AppTheme.secondaryBlue, size: 18),
                  SizedBox(width: 8),
                  Expanded(
                    child: Text(
                      'Latihan tidak disimpan. Kembali ke menu utama.',
                      style: TextStyle(fontSize: 12, color: AppTheme.secondaryBlue),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx),
            child: const Text('Lanjut Latihan'),
          ),
          ElevatedButton(
            onPressed: () {
              Navigator.pop(ctx);
              context.go('/home');
            },
            style: ElevatedButton.styleFrom(
              backgroundColor: AppTheme.primaryRed,
            ),
            child: const Text('Akhiri', style: TextStyle(color: Colors.white)),
          ),
        ],
      ),
    );
  }

  void _showSubmitConfirmation(BuildContext context) {
    final tryout = ref.read(tryoutProvider);
    if (tryout == null) return;

    final unanswered = tryout.totalCount - tryout.answeredCount;
    final ragu = tryout.flaggedQuestions.length;

    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (dialogContext) => AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        title: Row(
          children: [
            Icon(
              unanswered > 0 ? Icons.warning_amber : Icons.check_circle,
              color: unanswered > 0 ? AppTheme.warningOrange : AppTheme.successGreen,
            ),
            const SizedBox(width: 8),
            const Text('Kirim Jawaban?'),
          ],
        ),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Summary widget
            _buildSummaryRow(
              'Total Soal',
              '${tryout.totalCount}',
              Colors.grey.shade700,
            ),
            const SizedBox(height: 6),
            _buildSummaryRow(
              'Sudah Dijawab',
              '${tryout.answeredCount}',
              AppTheme.catAnswered,
            ),
            const SizedBox(height: 6),
            _buildSummaryRow(
              'Belum Dijawab',
              '$unanswered',
              unanswered > 0 ? AppTheme.catVisitedEmpty : Colors.grey,
            ),
            const SizedBox(height: 6),
            if (ragu > 0)
              _buildSummaryRow(
                'Ragu-ragu',
                '$ragu',
                AppTheme.catFlagged,
              ),
            const SizedBox(height: 16),
            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: unanswered > 0
                    ? AppTheme.warningOrange.withAlpha(15)
                    : AppTheme.successGreen.withAlpha(15),
                borderRadius: BorderRadius.circular(8),
                border: Border.all(
                  color: unanswered > 0
                      ? AppTheme.warningOrange.withAlpha(40)
                      : AppTheme.successGreen.withAlpha(40),
                ),
              ),
              child: Row(
                children: [
                  Icon(
                    unanswered > 0 ? Icons.info_outline : Icons.check_circle,
                    color: unanswered > 0 ? AppTheme.warningOrange : AppTheme.successGreen,
                    size: 18,
                  ),
                  const SizedBox(width: 8),
                  Expanded(
                    child: Text(
                      unanswered > 0
                          ? '$unanswered soal belum dijawab dan tidak akan dihitung.'
                          : 'Semua soal sudah dijawab!',
                      style: TextStyle(
                        fontSize: 12,
                        color: unanswered > 0
                            ? AppTheme.warningOrange
                            : AppTheme.successGreen,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(dialogContext),
            child: const Text('Cek Lagi'),
          ),
          ElevatedButton(
            onPressed: () async {
              Navigator.pop(dialogContext);
              await ref.read(tryoutProvider.notifier).finishTryout();
              if (dialogContext.mounted) {
                final sessionId = ref.read(tryoutProvider)?.sessionId ?? '';
                context.go('/result/$sessionId');
              }
            },
            style: ElevatedButton.styleFrom(
              backgroundColor: unanswered > 0
                  ? AppTheme.warningOrange
                  : AppTheme.successGreen,
            ),
            child: const Text('Kirim', style: TextStyle(color: Colors.white)),
          ),
        ],
      ),
    );
  }

  Widget _buildSummaryRow(String label, String value, Color color) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Text(label, style: TextStyle(fontSize: 14, color: Colors.grey.shade700)),
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 3),
          decoration: BoxDecoration(
            color: color.withAlpha(20),
            borderRadius: BorderRadius.circular(12),
          ),
          child: Text(
            value,
            style: TextStyle(
              fontWeight: FontWeight.bold,
              color: color,
              fontSize: 14,
            ),
          ),
        ),
      ],
    );
  }

  void _checkTimeWarnings(int remaining) {
    // 10 menit: kuning
    if (remaining == 600 && !_shownWarnings.contains(600)) {
      _shownWarnings.add(600);
      _showTimeWarningSnackBar(
        '10 menit tersisa! Perhatikan waktu kamu.',
        AppTheme.warningOrange,
        Icons.timer,
      );
    }
    // 5 menit: oranye
    if (remaining == 300 && !_shownWarnings.contains(300)) {
      _shownWarnings.add(300);
      HapticFeedback.heavyImpact();
      _showTimeWarningSnackBar(
        '5 menit tersisa! Segera selesaikan.',
        AppTheme.primaryRedLight,
        Icons.timer,
      );
    }
    // 1 menit: merah berkedip sudah dihandle TimerWidget
  }

  double _bottomPadding(BuildContext context) {
    // Extra bottom padding: nav buttons (~56) + safe area bottom
    final safeBottom = MediaQuery.of(context).padding.bottom;
    return 16 + 56 + safeBottom;
  }

  double _calcBottomNavBarHeight(BuildContext context) {
    // Navigation buttons bottom padding = safe area only (nav bar is below)
    return MediaQuery.of(context).padding.bottom;
  }

  void _showTimeWarningSnackBar(String message, Color color, IconData icon) {
    if (!mounted) return;
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Row(
          children: [
            Icon(icon, color: Colors.white, size: 20),
            const SizedBox(width: 10),
            Expanded(
              child: Text(
                message,
                style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w600),
              ),
            ),
          ],
        ),
        backgroundColor: color,
        duration: const Duration(seconds: 4),
        behavior: SnackBarBehavior.floating,
        margin: const EdgeInsets.all(16),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
      ),
    );
  }

  void _showTimeUpOverlay(BuildContext context) {
    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (ctx) => AlertDialog(
        backgroundColor: AppTheme.primaryRed,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Icon(Icons.timer_off, color: Colors.white, size: 64),
            const SizedBox(height: 16),
            const Text(
              'WAKTU HABIS!',
              style: TextStyle(
                color: Colors.white,
                fontSize: 24,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 8),
            Text(
              'Jawaban kamu akan dikirim otomatis.',
              style: TextStyle(
                color: Colors.white.withAlpha(200),
                fontSize: 14,
              ),
              textAlign: TextAlign.center,
            ),
          ],
        ),
        actions: [
          Center(
            child: ElevatedButton(
              onPressed: () async {
                Navigator.pop(ctx);
                await ref.read(tryoutProvider.notifier).finishTryout();
                if (ctx.mounted) {
                  final sessionId = ref.read(tryoutProvider)?.sessionId ?? '';
                  context.go('/result/$sessionId');
                }
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.white,
                foregroundColor: AppTheme.primaryRed,
                padding: const EdgeInsets.symmetric(horizontal: 32, vertical: 12),
              ),
              child: const Text('LIHAT HASIL', style: TextStyle(fontWeight: FontWeight.bold)),
            ),
          ),
        ],
      ),
    );
  }
}
