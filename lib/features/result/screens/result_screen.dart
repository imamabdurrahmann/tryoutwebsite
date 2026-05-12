import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import '../../../core/theme/app_theme.dart';
import '../../../core/constants/app_constants.dart';
import '../../../core/utils/celebration_widget.dart';
import '../../../providers/tryout_provider.dart';

class ResultScreen extends ConsumerWidget {
  final String sessionId;

  const ResultScreen({super.key, required this.sessionId});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final sessionAsync = ref.watch(sessionDetailProvider(sessionId));
    final theme = Theme.of(context);

    return Scaffold(
      backgroundColor: theme.scaffoldBackgroundColor,
      body: sessionAsync.when(
        data: (session) {
          if (session == null) {
            return const Center(child: Text('Data tidak ditemukan'));
          }

          // ===== DATA DRIVEN: cek paket untuk conditional rendering =====
          final isFull = session.isFull;
          final isTwkOnly = session.isTwkOnly;
          final isTiuOnly = session.isTiuOnly;
          final isTkpOnly = session.isTkpOnly;
          final maxTotal = session.maxTotalScore;

          return Stack(
            children: [
              SafeArea(
            child: Center(
              child: ConstrainedBox(
                constraints: const BoxConstraints(maxWidth: 900),
                child: CustomScrollView(
              slivers: [
                // ===== Header =====
                SliverToBoxAdapter(
                  child: _buildHeader(context, session, isFull),
                ),
                SliverPadding(
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  sliver: SliverList(
                    delegate: SliverChildListDelegate([
                      const SizedBox(height: 20),

                      // Overall Status Banner — hanya FULL yang punya 3 badge
                      _buildOverallBanner(context, session, isFull, isTwkOnly, isTiuOnly, isTkpOnly),
                      const SizedBox(height: 20),

                      // Total Score Card — max score berubah sesuai paket
                      _buildTotalScoreCard(context, session, maxTotal),
                      const SizedBox(height: 12),

                      // Participant ID Card
                      _buildParticipantCard(context, session),
                      const SizedBox(height: 12),

                      // Motivation Card
                      if (!session.overallPassed) _buildMotivationCard(context, isFull),

                      const SizedBox(height: 16),

                      // Category Detail Cards — sembunyikan yang tidak ikut
                      if (!isTiuOnly && !isTkpOnly)
                        _buildCategoryCard(context, 'TWK', 'Tes Wawasan Kebangsaan',
                            session.twkScore, AppConstants.twkPassingGrade, session.twkQuestionCount, session),
                      if (!isTwkOnly && !isTkpOnly)
                        _buildCategoryCard(context, 'TIU', 'Tes Intelegensi Umum',
                            session.tiuScore, AppConstants.tiuPassingGrade, session.tiuQuestionCount, session),
                      if (!isTwkOnly && !isTiuOnly)
                        _buildCategoryCard(context, 'TKP', 'Tes Karakteristik Pribadi',
                            session.tkpScore, AppConstants.tkpPassingGrade, session.tkpQuestionCount, session,
                            isTkp: true),

                      const SizedBox(height: 24),

                      // Action Buttons
                      SizedBox(
                        width: double.infinity,
                        child: OutlinedButton.icon(
                          onPressed: () {
                            context.push('/review/$sessionId');
                          },
                          icon: const Icon(Icons.menu_book),
                          label: const Text('Lihat Pembahasan'),
                          style: OutlinedButton.styleFrom(
                            padding: const EdgeInsets.symmetric(vertical: 14),
                            side: const BorderSide(color: AppTheme.primaryRed, width: 2),
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(12),
                            ),
                          ),
                        ),
                      ),
                      const SizedBox(height: 10),
                      SizedBox(
                        width: double.infinity,
                        child: OutlinedButton.icon(
                          onPressed: () {
                            context.go('/home');
                          },
                          icon: const Icon(Icons.home),
                          label: const Text('Kembali ke Beranda'),
                          style: OutlinedButton.styleFrom(
                            padding: const EdgeInsets.symmetric(vertical: 14),
                            side: BorderSide(color: Colors.grey.shade400, width: 1.5),
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(12),
                            ),
                          ),
                        ),
                      ),
                      const SizedBox(height: 10),
                      SizedBox(
                        width: double.infinity,
                        child: ElevatedButton.icon(
                          onPressed: () {
                            context.push('/tryout/${session.packageType}');
                          },
                          icon: const Icon(Icons.refresh),
                          label: Text(session.overallPassed ? 'Coba Lagi' : 'Ulangi Try Out'),
                          style: ElevatedButton.styleFrom(
                            backgroundColor: session.overallPassed
                                ? AppTheme.secondaryBlue
                                : AppTheme.primaryRed,
                            foregroundColor: Colors.white,
                            padding: const EdgeInsets.symmetric(vertical: 14),
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(12),
                            ),
                          ),
                        ),
                      ),
                      const SizedBox(height: 24),
                    ]),
                  ),
                ),
              ],
            ),
          ),
            ),
          ),
              // Confetti overlay saat LULUS
              if (session.overallPassed)
                RepaintBoundary(
                  child: Positioned.fill(
                    child: IgnorePointer(
                      child: CelebrationWidget(show: session.overallPassed),
                    ),
                  ),
                ),
            ],
          );
        },
        loading: () => const Center(child: CircularProgressIndicator()),
        error: (e, _) => Center(child: Text('Error: $e')),
      ),
    );
  }

  Widget _buildHeader(BuildContext context, dynamic session, bool isFull) {
    // Header gradient berubah sesuai hasil lulus/gagal
    return Container(
      padding: const EdgeInsets.fromLTRB(20, 20, 20, 24),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: session.overallPassed
              ? [AppTheme.successGreen, AppTheme.successGreen.withAlpha(200)]
              : [AppTheme.primaryRed, AppTheme.primaryRedDark],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: const BorderRadius.only(
          bottomLeft: Radius.circular(32),
          bottomRight: Radius.circular(32),
        ),
        boxShadow: [
          BoxShadow(
            color: (session.overallPassed ? AppTheme.successGreen : AppTheme.primaryRed)
                .withAlpha(80),
            blurRadius: 24,
            offset: const Offset(0, 8),
          ),
        ],
      ),
      child: Column(
        children: [
          Row(
            children: [
              Container(
                padding: const EdgeInsets.all(10),
                decoration: BoxDecoration(
                  color: Colors.white.withAlpha(25),
                  shape: BoxShape.circle,
                ),
                child: Icon(
                  session.overallPassed ? Icons.emoji_events : Icons.sentiment_dissatisfied,
                  color: Colors.white,
                  size: 28,
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      session.overallPassed ? 'SELAMAT! LULUS!' : 'GAGAL, COBA LAGI',
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 20,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    Text(
                      session.packageLabel,
                      style: TextStyle(
                        color: Colors.white.withAlpha(180),
                        fontSize: 13,
                      ),
                    ),
                  ],
                ),
              ),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                decoration: BoxDecoration(
                  color: Colors.white.withAlpha(25),
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(color: Colors.white24),
                ),
                child: Text(
                  '${session.durationMinutes} menit',
                  style: const TextStyle(color: Colors.white, fontSize: 12, fontWeight: FontWeight.w500),
                ),
              ),
            ],
          ),
          if (!session.overallPassed) ...[
            const SizedBox(height: 12),
            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: Colors.white.withAlpha(20),
                borderRadius: BorderRadius.circular(12),
              ),
              child: Row(
                children: [
                  Icon(Icons.info_outline, color: Colors.white.withAlpha(200), size: 18),
                  const SizedBox(width: 8),
                  Expanded(
                    child: Text(
                      isFull
                          ? 'Kamu harus lulus di SEMUA kategori (TWK, TIU, TKP)'
                          : session.passingGradeInfo,
                      style: TextStyle(color: Colors.white.withAlpha(220), fontSize: 12),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ],
      ),
    );
  }

  Widget _buildOverallBanner(
      BuildContext context, dynamic session,
      bool isFull, bool isTwkOnly, bool isTiuOnly, bool isTkpOnly) {
    // Single-category tests show one badge only
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Theme.of(context).cardColor,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.grey.shade200),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        children: [
          if (!isTiuOnly && !isTkpOnly)
            _buildPassBadge(context, 'TWK', session.twkScore, AppConstants.twkPassingGrade, session.twkPassed),
          if (!isTwkOnly && !isTiuOnly && !isTkpOnly && session.twkQuestionCount > 0)
            Container(width: 1, height: 50, color: Colors.grey.shade300),
          if (!isTwkOnly && !isTkpOnly)
            _buildPassBadge(context, 'TIU', session.tiuScore, AppConstants.tiuPassingGrade, session.tiuPassed),
          if (!isTwkOnly && !isTiuOnly)
            Container(width: 1, height: 50, color: Colors.grey.shade300),
          if (!isTwkOnly && !isTiuOnly)
            _buildPassBadge(context, 'TKP', session.tkpScore, AppConstants.tkpPassingGrade, session.tkpPassed),
        ],
      ),
    );
  }

  Widget _buildPassBadge(BuildContext context, String label, int score, int passing, bool passed) {
    return Column(
      children: [
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
          decoration: BoxDecoration(
            color: passed
                ? AppTheme.successGreen.withAlpha(20)
                : AppTheme.errorRed.withAlpha(20),
            borderRadius: BorderRadius.circular(20),
            border: Border.all(
              color: passed ? AppTheme.successGreen.withAlpha(50) : AppTheme.errorRed.withAlpha(50),
            ),
          ),
          child: Text(
            passed ? 'LULUS' : 'TIDAK LULUS',
            style: TextStyle(
              color: passed ? AppTheme.successGreen : AppTheme.errorRed,
              fontWeight: FontWeight.bold,
              fontSize: 11,
            ),
          ),
        ),
        const SizedBox(height: 6),
        Text(
          '$score',
          style: Theme.of(context).textTheme.titleLarge?.copyWith(
                fontWeight: FontWeight.bold,
                color: passed ? AppTheme.successGreen : AppTheme.errorRed,
              ),
        ),
        Text(
          '/ $passing',
          style: TextStyle(color: Colors.grey.shade500, fontSize: 11),
        ),
      ],
    );
  }

  Widget _buildTotalScoreCard(BuildContext context, dynamic session, int maxTotal) {
    // Skor maksimal berubah sesuai paket:
    // FULL=550, TWK_ONLY=150, TIU_ONLY=175, TKP_ONLY=225
    final progress = (session.totalScore / maxTotal).clamp(0.0, 1.0);

    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Theme.of(context).cardColor,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.grey.shade200),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withAlpha(12),
            blurRadius: 8,
            offset: const Offset(0, 2),
          ),
        ],
      ),
      child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Total Skor',
                    style: TextStyle(color: Colors.grey.shade600, fontSize: 13),
                  ),
                  const SizedBox(height: 4),
                  TweenAnimationBuilder<int>(
                    tween: IntTween(begin: 0, end: session.totalScore),
                    duration: const Duration(milliseconds: 1500),
                    curve: Curves.easeOut,
                    builder: (context, value, child) {
                      return Row(
                        crossAxisAlignment: CrossAxisAlignment.baseline,
                        textBaseline: TextBaseline.alphabetic,
                        children: [
                          Text(
                            '$value',
                            style: Theme.of(context).textTheme.displaySmall?.copyWith(
                                  fontWeight: FontWeight.bold,
                                  color: AppTheme.primaryRed,
                                ),
                          ),
                          Text(
                            ' / $maxTotal',
                            style: TextStyle(color: Colors.grey.shade500, fontSize: 16),
                          ),
                        ],
                      );
                    },
                  ),
                ],
              ),
              TweenAnimationBuilder<double>(
                tween: Tween(begin: 0, end: session.overallPassed ? 1.0 : 0.0),
                duration: const Duration(milliseconds: 800),
                curve: Curves.elasticOut,
                builder: (context, value, child) {
                  return Container(
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(
                      color: AppTheme.primaryRed.withAlpha(15),
                      shape: BoxShape.circle,
                    ),
                    child: Icon(
                      session.overallPassed ? Icons.check_circle : Icons.cancel,
                      color: session.overallPassed ? AppTheme.successGreen : AppTheme.errorRed,
                      size: 32,
                    ),
                  );
                },
              ),
            ],
          ),
          const SizedBox(height: 16),
          ClipRRect(
            borderRadius: BorderRadius.circular(8),
            child: TweenAnimationBuilder<double>(
              tween: Tween(begin: 0, end: progress),
              duration: const Duration(milliseconds: 1500),
              curve: Curves.easeOut,
              builder: (context, value, child) {
                return LinearProgressIndicator(
                  value: value,
                  backgroundColor: Colors.grey.shade200,
                  valueColor: AlwaysStoppedAnimation(
                    session.overallPassed ? AppTheme.successGreen : AppTheme.warningOrange,
                  ),
                  minHeight: 10,
                );
              },
            ),
          ),
          const SizedBox(height: 8),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                'Skor Kamu',
                style: TextStyle(color: Colors.grey.shade500, fontSize: 11),
              ),
              TweenAnimationBuilder<double>(
                tween: Tween(begin: 0, end: progress),
                duration: const Duration(milliseconds: 1500),
                builder: (context, value, child) {
                  return Text(
                    '${(value * 100).toStringAsFixed(0)}% dari passing grade',
                    style: TextStyle(color: Colors.grey.shade500, fontSize: 11),
                  );
                },
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildCategoryCard(
    BuildContext context,
    String category,
    String label,
    int score,
    int passingGrade,
    int totalInSession,
    dynamic session, {
    bool isTkp = false,
  }) {
    final bool passed;
    final int correct;
    final int wrong;
    final int unanswered;
    final Color color;

    if (category == 'TWK') {
      passed = session.twkPassed;
      correct = session.twkCorrect;
      wrong = session.twkWrong;
      unanswered = session.twkUnanswered;
      color = AppTheme.secondaryBlue;
    } else if (category == 'TIU') {
      passed = session.tiuPassed;
      correct = session.tiuCorrect;
      wrong = session.tiuWrong;
      unanswered = session.tiuUnanswered;
      color = AppTheme.warningOrange;
    } else {
      passed = session.tkpPassed;
      correct = 0;
      wrong = 0;
      unanswered = session.tkpUnanswered;
      color = AppTheme.successGreen;
    }

    final progress = (score / passingGrade).clamp(0.0, 1.0);
    final isOver = score >= passingGrade;

    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Theme.of(context).cardColor,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: passed ? color.withAlpha(60) : Colors.grey.shade200,
          width: passed ? 2 : 1,
        ),
      ),
      child: Column(
        children: [
          Row(
            children: [
              Container(
                width: 44,
                height: 44,
                decoration: BoxDecoration(
                  color: color.withAlpha(20),
                  shape: BoxShape.circle,
                  border: Border.all(color: color.withAlpha(50)),
                ),
                child: Center(
                  child: Text(
                    category,
                    style: TextStyle(
                      color: color,
                      fontWeight: FontWeight.bold,
                      fontSize: 12,
                    ),
                  ),
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      label,
                      style: Theme.of(context).textTheme.titleSmall?.copyWith(
                            fontWeight: FontWeight.bold,
                          ),
                    ),
                    Text(
                      '$totalInSession soal',
                      style: TextStyle(color: Colors.grey.shade500, fontSize: 11),
                    ),
                  ],
                ),
              ),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                decoration: BoxDecoration(
                  color: isOver
                      ? AppTheme.successGreen.withAlpha(20)
                      : AppTheme.errorRed.withAlpha(20),
                  borderRadius: BorderRadius.circular(20),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(
                      isOver ? Icons.check_circle : Icons.cancel,
                      size: 14,
                      color: isOver ? AppTheme.successGreen : AppTheme.errorRed,
                    ),
                    const SizedBox(width: 4),
                    Text(
                      isOver ? 'LULUS' : 'TIDAK LULUS',
                      style: TextStyle(
                        color: isOver ? AppTheme.successGreen : AppTheme.errorRed,
                        fontWeight: FontWeight.bold,
                        fontSize: 12,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 16),
          Row(
            children: [
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Text(
                        '$score',
                        style: Theme.of(context).textTheme.headlineSmall?.copyWith(
                              fontWeight: FontWeight.bold,
                              color: color,
                            ),
                      ),
                      Text(
                        ' / $passingGrade',
                        style: TextStyle(color: Colors.grey.shade600, fontSize: 16),
                      ),
                    ],
                  ),
                  Text(
                    'Passing Grade',
                    style: TextStyle(color: Colors.grey.shade500, fontSize: 11),
                  ),
                ],
              ),
              const Spacer(),
              Column(
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  Text(
                    'Max: ${isTkp ? 225 : 100}',
                    style: TextStyle(color: Colors.grey.shade400, fontSize: 11),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    isTkp
                        ? 'A=5, B=4, C=3, D=2, E=1'
                        : 'Benar = 5 poin',
                    style: TextStyle(color: Colors.grey.shade400, fontSize: 10),
                  ),
                ],
              ),
            ],
          ),
          const SizedBox(height: 14),
          ClipRRect(
            borderRadius: BorderRadius.circular(6),
            child: LinearProgressIndicator(
              value: progress,
              backgroundColor: Colors.grey.shade200,
              valueColor: AlwaysStoppedAnimation(color),
              minHeight: 8,
            ),
          ),
          const SizedBox(height: 12),
          // Stats row
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: isTkp
                ? [
                    _buildStatChip(AppTheme.successGreen, '${totalInSession - unanswered}', 'Dijawab'),
                    _buildStatChip(Colors.grey.shade400, '$unanswered', 'Kosong'),
                  ]
                : [
                    _buildStatChip(AppTheme.successGreen, '$correct', 'Benar'),
                    _buildStatChip(AppTheme.errorRed, '$wrong', 'Salah'),
                    _buildStatChip(Colors.grey.shade400, '$unanswered', 'Kosong'),
                  ],
          ),
        ],
      ),
    );
  }

  Widget _buildMotivationCard(BuildContext context, bool isFull) {
    String desc;
    if (isFull) {
      desc = '110 soal dalam 100 menit — latihlah kecepatan membacamu untuk bisa finish tepat waktu.';
    } else {
      desc = 'Fokus pada kategori yang kamu ikuti. Ulangi latihan untuk meningkatkan skor.';
    }
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [
            AppTheme.primaryRed.withAlpha(15),
            AppTheme.secondaryBlue.withAlpha(15),
          ],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: AppTheme.primaryRed.withAlpha(30),
          width: 1,
        ),
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: AppTheme.warningOrange.withAlpha(25),
              shape: BoxShape.circle,
            ),
            child: const Icon(
              Icons.speed,
              color: AppTheme.warningOrange,
              size: 24,
            ),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Ingat, tantangan asli adalah kecepatan!',
                  style: Theme.of(context).textTheme.titleSmall?.copyWith(
                        fontWeight: FontWeight.bold,
                        color: AppTheme.primaryRed,
                      ),
                ),
                const SizedBox(height: 4),
                Text(
                  desc,
                  style: Theme.of(context).textTheme.bodySmall?.copyWith(
                        color: Colors.grey.shade700,
                        height: 1.4,
                      ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildStatChip(Color color, String value, String label) {
    return Column(
      children: [
        Text(
          value,
          style: TextStyle(
            color: color,
            fontWeight: FontWeight.bold,
            fontSize: 18,
          ),
        ),
        Text(
          label,
          style: TextStyle(color: Colors.grey.shade500, fontSize: 10),
        ),
      ],
    );
  }

  Widget _buildParticipantCard(BuildContext context, dynamic session) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Theme.of(context).cardColor,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.grey.shade200),
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: AppTheme.secondaryBlue.withAlpha(15),
              shape: BoxShape.circle,
            ),
            child: const Icon(
              Icons.badge,
              color: AppTheme.secondaryBlue,
              size: 24,
            ),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Peserta TryOutCPNSbyIMAM',
                  style: Theme.of(context).textTheme.titleSmall?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                ),
                const SizedBox(height: 4),
                Text(
                  'ID Sesi: ${session.sessionId.substring(session.sessionId.length > 8 ? session.sessionId.length - 8 : 0)}',
                  style: TextStyle(
                    fontSize: 12,
                    color: Colors.grey.shade600,
                    fontFamily: 'monospace',
                  ),
                ),
              ],
            ),
          ),
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
            decoration: BoxDecoration(
              color: session.overallPassed
                  ? AppTheme.successGreen.withAlpha(15)
                  : AppTheme.errorRed.withAlpha(15),
              borderRadius: BorderRadius.circular(20),
              border: Border.all(
                color: session.overallPassed
                    ? AppTheme.successGreen.withAlpha(50)
                    : AppTheme.errorRed.withAlpha(50),
              ),
            ),
            child: Text(
              session.overallPassed ? 'LULUS' : 'TIDAK LULUS',
              style: TextStyle(
                color: session.overallPassed ? AppTheme.successGreen : AppTheme.errorRed,
                fontWeight: FontWeight.bold,
                fontSize: 13,
              ),
            ),
          ),
        ],
      ),
    );
  }
}