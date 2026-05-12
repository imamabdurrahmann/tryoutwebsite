import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:intl/intl.dart';
import '../../../core/theme/app_theme.dart';
import '../../../data/models/tryout_session.dart';
import '../../../providers/tryout_provider.dart';
import '../widgets/progress_chart.dart';

class HistoryScreen extends ConsumerStatefulWidget {
  const HistoryScreen({super.key});

  @override
  ConsumerState<HistoryScreen> createState() => _HistoryScreenState();
}

class _HistoryScreenState extends ConsumerState<HistoryScreen>
    with SingleTickerProviderStateMixin {
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // Watch all providers - no direct data loading in build()
    final sessionsAsync = ref.watch(sessionsNotifierProvider);
    final progressDataAsync = ref.watch(progressDataProvider);
    final accuracyAsync = ref.watch(categoryAccuracyProvider);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Riwayat Try Out'),
        actions: [
          IconButton(
            icon: const Icon(Icons.refresh),
            onPressed: () {
              ref.read(sessionsNotifierProvider.notifier).refresh();
            },
          ),
        ],
        bottom: TabBar(
          controller: _tabController,
          tabs: const [
            Tab(text: 'Riwayat'),
            Tab(text: 'Statistik'),
          ],
          indicatorColor: Colors.white,
          labelColor: Colors.white,
          unselectedLabelColor: Colors.white70,
        ),
      ),
      body: sessionsAsync.when(
        loading: () => const Center(child: CircularProgressIndicator()),
        error: (error, stack) => Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(Icons.error_outline, size: 48, color: Colors.grey.shade400),
              const SizedBox(height: 16),
              Text('Error loading data', style: TextStyle(color: Colors.grey.shade600)),
              const SizedBox(height: 8),
              ElevatedButton(
                onPressed: () => ref.read(sessionsNotifierProvider.notifier).refresh(),
                child: const Text('Retry'),
              ),
            ],
          ),
        ),
        data: (sessions) => Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 900),
            child: TabBarView(
              controller: _tabController,
              children: [
                // Tab 1: History List
                _HistoryListTab(sessions: sessions),
                // Tab 2: Statistics
                _StatsTab(
                  sessions: sessions,
                  progressDataAsync: progressDataAsync,
                  accuracyAsync: accuracyAsync,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _HistoryListTab extends StatelessWidget {
  final List<TryoutSession> sessions;

  const _HistoryListTab({required this.sessions});

  @override
  Widget build(BuildContext context) {
    if (sessions.isEmpty) {
      return Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.history, size: 64, color: Colors.grey.shade400),
            const SizedBox(height: 16),
            Text(
              'Belum ada riwayat',
              style: TextStyle(color: Colors.grey.shade600),
            ),
            const SizedBox(height: 8),
            ElevatedButton(
              onPressed: () => context.go('/home'),
              child: const Text('Mulai Try Out'),
            ),
          ],
        ),
      );
    }

    return ListView.builder(
      padding: const EdgeInsets.all(16),
      itemExtent: 90, // Fixed height for faster scroll performance
      itemCount: sessions.length,
      itemBuilder: (context, index) {
        final session = sessions[index];
        return _SessionCard(session: session);
      },
    );
  }
}

class _SessionCard extends StatelessWidget {
  final TryoutSession session;

  const _SessionCard({required this.session});

  @override
  Widget build(BuildContext context) {
    final dateFormat = DateFormat('dd MMM yyyy, HH:mm');

    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: InkWell(
        onTap: () => context.push('/result/${session.sessionId}'),
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Row(
            children: [
              Container(
                width: 50,
                height: 50,
                decoration: BoxDecoration(
                  color: session.overallPassed
                      ? AppTheme.successGreen.withAlpha(26)
                      : AppTheme.errorRed.withAlpha(26),
                  shape: BoxShape.circle,
                ),
                child: Icon(
                  session.overallPassed ? Icons.check_circle : Icons.cancel,
                  color: session.overallPassed
                      ? AppTheme.successGreen
                      : AppTheme.errorRed,
                  size: 28,
                ),
              ),
              const SizedBox(width: 16),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      session.packageLabel,
                      style: Theme.of(context).textTheme.titleSmall?.copyWith(
                            fontWeight: FontWeight.bold,
                          ),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      dateFormat.format(session.startTime),
                      style: const TextStyle(color: Colors.grey, fontSize: 12),
                    ),
                  ],
                ),
              ),
              Column(
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  Text(
                    '${session.totalScore}',
                    style: Theme.of(context).textTheme.titleLarge?.copyWith(
                          fontWeight: FontWeight.bold,
                          color: AppTheme.primaryRed,
                        ),
                  ),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                    decoration: BoxDecoration(
                      color: session.overallPassed
                          ? AppTheme.successGreen.withAlpha(26)
                          : AppTheme.errorRed.withAlpha(26),
                      borderRadius: BorderRadius.circular(10),
                    ),
                    child: Text(
                      session.overallPassed ? 'LULUS' : 'TL',
                      style: TextStyle(
                        fontSize: 10,
                        fontWeight: FontWeight.bold,
                        color: session.overallPassed
                            ? AppTheme.successGreen
                            : AppTheme.errorRed,
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(width: 8),
              const Icon(Icons.chevron_right, color: Colors.grey),
            ],
          ),
        ),
      ),
    );
  }
}

class _StatsTab extends StatelessWidget {
  final List<TryoutSession> sessions;
  final AsyncValue<List<Map<String, dynamic>>> progressDataAsync;
  final AsyncValue<Map<String, double>> accuracyAsync;

  const _StatsTab({
    required this.sessions,
    required this.progressDataAsync,
    required this.accuracyAsync,
  });

  @override
  Widget build(BuildContext context) {
    if (sessions.isEmpty) {
      return Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.bar_chart, size: 64, color: Colors.grey.shade400),
            const SizedBox(height: 16),
            Text(
              'Belum ada data statistik',
              style: TextStyle(color: Colors.grey.shade600),
            ),
            const SizedBox(height: 8),
            const Text(
              'Selesaikan try out untuk melihat statistik',
              style: TextStyle(color: Colors.grey, fontSize: 12),
            ),
          ],
        ),
      );
    }

    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            'Progres Skor',
            style: Theme.of(context).textTheme.titleMedium?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
          ),
          const SizedBox(height: 12),
          progressDataAsync.when(
            loading: () => const Center(child: CircularProgressIndicator()),
            error: (_, __) => const Text('Error loading progress data'),
            data: (progressData) => ProgressChart(data: progressData),
          ),
          const SizedBox(height: 24),

          Text(
            'Akurasi per Kategori',
            style: Theme.of(context).textTheme.titleMedium?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
          ),
          const SizedBox(height: 12),
          accuracyAsync.when(
            loading: () => const Center(child: CircularProgressIndicator()),
            error: (_, __) => const Text('Error loading accuracy data'),
            data: (accuracy) => _AccuracyCard(accuracy: accuracy),
          ),
          const SizedBox(height: 24),

          // === NEW: Analisis Kelemahan ===
          _WeaknessAnalysis(sessions: sessions),
          const SizedBox(height: 24),

          _SummaryCard(sessions: sessions),
        ],
      ),
    );
  }
}

class _AccuracyCard extends StatelessWidget {
  final Map<String, double> accuracy;

  const _AccuracyCard({required this.accuracy});

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            _AccuracyRow('TWK', accuracy['TWK'] ?? 0, AppTheme.secondaryBlue),
            const SizedBox(height: 12),
            _AccuracyRow('TIU', accuracy['TIU'] ?? 0, AppTheme.warningOrange),
            const SizedBox(height: 12),
            _AccuracyRow('TKP', accuracy['TKP'] ?? 0, AppTheme.successGreen),
          ],
        ),
      ),
    );
  }
}

class _AccuracyRow extends StatelessWidget {
  final String category;
  final double value;
  final Color color;

  const _AccuracyRow(this.category, this.value, this.color);

  @override
  Widget build(BuildContext context) {
    final percentage = value.clamp(0.0, 100.0);

    return Row(
      children: [
        SizedBox(
          width: 50,
          child: Text(category, style: const TextStyle(fontWeight: FontWeight.bold)),
        ),
        Expanded(
          child: ClipRRect(
            borderRadius: BorderRadius.circular(8),
            child: LinearProgressIndicator(
              value: percentage / 100,
              backgroundColor: Colors.grey.shade200,
              valueColor: AlwaysStoppedAnimation(color),
              minHeight: 12,
            ),
          ),
        ),
        const SizedBox(width: 12),
        SizedBox(
          width: 50,
          child: Text(
            '${percentage.toStringAsFixed(0)}%',
            style: TextStyle(color: color, fontWeight: FontWeight.bold),
          ),
        ),
      ],
    );
  }
}

class _SummaryCard extends StatelessWidget {
  final List<TryoutSession> sessions;

  const _SummaryCard({required this.sessions});

  @override
  Widget build(BuildContext context) {
    if (sessions.isEmpty) return const SizedBox();

    final totalSessions = sessions.length;
    final passedSessions = sessions.where((s) => s.overallPassed).length;
    final avgScore = sessions.fold<int>(0, (sum, s) => sum + s.totalScore) ~/ totalSessions;

    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Ringkasan',
              style: Theme.of(context).textTheme.titleSmall?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
            ),
            const SizedBox(height: 16),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                _buildSummaryItem(context, '$totalSessions', 'Total Sesi', Colors.blue),
                _buildSummaryItem(context, '$passedSessions', 'Lulus', AppTheme.successGreen),
                _buildSummaryItem(context, '$avgScore', 'Rata-rata', AppTheme.primaryRed),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSummaryItem(BuildContext context, String value, String label, Color color) {
    return Column(
      children: [
        Text(
          value,
          style: Theme.of(context).textTheme.headlineSmall?.copyWith(
                fontWeight: FontWeight.bold,
                color: color,
              ),
        ),
        Text(label, style: const TextStyle(color: Colors.grey, fontSize: 12)),
      ],
    );
  }
}

class _WeaknessAnalysis extends StatelessWidget {
  final List<TryoutSession> sessions;

  const _WeaknessAnalysis({required this.sessions});

  @override
  Widget build(BuildContext context) {
    if (sessions.length < 2) {
      return Card(
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              Icon(Icons.analytics_outlined, size: 40, color: Colors.grey.shade400),
              const SizedBox(height: 8),
              Text(
                'Selesaikan minimal 2 sesi try out untuk melihat analisis kelemahan',
                style: TextStyle(color: Colors.grey.shade600, fontSize: 13),
                textAlign: TextAlign.center,
              ),
            ],
          ),
        ),
      );
    }

    final categories = <String, _CatAnalysis>{};

    final twkS = sessions.where((s) => s.twkQuestionCount > 0).toList();
    if (twkS.isNotEmpty) {
      final avg = twkS.fold<int>(0, (s, e) => s + e.twkScore) / twkS.length;
      final pr = twkS.where((s) => s.twkPassed).length / twkS.length * 100;
      double tr = 0;
      if (twkS.length >= 2) tr = (twkS.last.twkScore - twkS[twkS.length - 2].twkScore).toDouble();
      categories['TWK'] = _CatAnalysis(avg, 65, pr, tr, AppTheme.secondaryBlue);
    }

    final tiuS = sessions.where((s) => s.tiuQuestionCount > 0).toList();
    if (tiuS.isNotEmpty) {
      final avg = tiuS.fold<int>(0, (s, e) => s + e.tiuScore) / tiuS.length;
      final pr = tiuS.where((s) => s.tiuPassed).length / tiuS.length * 100;
      double tr = 0;
      if (tiuS.length >= 2) tr = (tiuS.last.tiuScore - tiuS[tiuS.length - 2].tiuScore).toDouble();
      categories['TIU'] = _CatAnalysis(avg, 80, pr, tr, AppTheme.warningOrange);
    }

    final tkpS = sessions.where((s) => s.tkpQuestionCount > 0).toList();
    if (tkpS.isNotEmpty) {
      final avg = tkpS.fold<int>(0, (s, e) => s + e.tkpScore) / tkpS.length;
      final pr = tkpS.where((s) => s.tkpPassed).length / tkpS.length * 100;
      double tr = 0;
      if (tkpS.length >= 2) tr = (tkpS.last.tkpScore - tkpS[tkpS.length - 2].tkpScore).toDouble();
      categories['TKP'] = _CatAnalysis(avg, 166, pr, tr, AppTheme.successGreen);
    }

    final sorted = categories.entries.toList()
      ..sort((a, b) => (a.value.avg / a.value.pg).compareTo(b.value.avg / b.value.pg));

    final weakest = sorted.isNotEmpty ? sorted.first : null;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'Analisis Kelemahan',
          style: Theme.of(context).textTheme.titleMedium?.copyWith(fontWeight: FontWeight.bold),
        ),
        const SizedBox(height: 12),
        if (weakest != null)
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(
              gradient: LinearGradient(colors: [
                weakest.value.color.withAlpha(20),
                weakest.value.color.withAlpha(8),
              ]),
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: weakest.value.color.withAlpha(40)),
            ),
            child: Row(
              children: [
                Icon(Icons.lightbulb_outline, color: weakest.value.color, size: 24),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        'Fokuskan latihan pada ${weakest.key}',
                        style: TextStyle(fontWeight: FontWeight.bold, color: weakest.value.color, fontSize: 13),
                      ),
                      const SizedBox(height: 2),
                      Text(
                        'Rata-rata skor ${weakest.value.avg.toStringAsFixed(0)} dari passing grade ${weakest.value.pg} (${weakest.value.pr.toStringAsFixed(0)}% lulus)',
                        style: TextStyle(color: Colors.grey.shade700, fontSize: 12),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        const SizedBox(height: 12),
        Card(
          child: Padding(
            padding: const EdgeInsets.all(16),
            child: Column(
              children: [
                for (int i = 0; i < sorted.length; i++) ...[
                  _WeaknessRow(category: sorted[i].key, analysis: sorted[i].value),
                  if (i < sorted.length - 1) const SizedBox(height: 16),
                ],
              ],
            ),
          ),
        ),
      ],
    );
  }
}

class _WeaknessRow extends StatelessWidget {
  final String category;
  final _CatAnalysis analysis;

  const _WeaknessRow({required this.category, required this.analysis});

  @override
  Widget build(BuildContext context) {
    final ratio = (analysis.avg / analysis.pg).clamp(0.0, 1.0);
    final passing = analysis.avg >= analysis.pg;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          children: [
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
              decoration: BoxDecoration(
                color: analysis.color.withAlpha(20),
                borderRadius: BorderRadius.circular(6),
              ),
              child: Text(category, style: TextStyle(fontWeight: FontWeight.bold, color: analysis.color, fontSize: 12)),
            ),
            const Spacer(),
            Icon(
              analysis.trend > 0 ? Icons.trending_up : analysis.trend < 0 ? Icons.trending_down : Icons.trending_flat,
              color: analysis.trend > 0 ? AppTheme.successGreen : analysis.trend < 0 ? AppTheme.errorRed : Colors.grey,
              size: 18,
            ),
            const SizedBox(width: 4),
            Text(
              '${analysis.trend > 0 ? '+' : ''}${analysis.trend.toStringAsFixed(0)}',
              style: TextStyle(
                fontSize: 11, fontWeight: FontWeight.bold,
                color: analysis.trend > 0 ? AppTheme.successGreen : analysis.trend < 0 ? AppTheme.errorRed : Colors.grey,
              ),
            ),
            const SizedBox(width: 12),
            Text(
              '${analysis.avg.toStringAsFixed(0)}/${analysis.pg}',
              style: TextStyle(fontWeight: FontWeight.bold, color: passing ? AppTheme.successGreen : analysis.color, fontSize: 13),
            ),
          ],
        ),
        const SizedBox(height: 6),
        ClipRRect(
          borderRadius: BorderRadius.circular(4),
          child: LinearProgressIndicator(
            value: ratio,
            backgroundColor: Colors.grey.shade200,
            valueColor: AlwaysStoppedAnimation(passing ? AppTheme.successGreen : analysis.color),
            minHeight: 8,
          ),
        ),
        const SizedBox(height: 4),
        Text('Lulus: ${analysis.pr.toStringAsFixed(0)}% sesi', style: TextStyle(fontSize: 10, color: Colors.grey.shade500)),
      ],
    );
  }
}

class _CatAnalysis {
  final double avg;
  final int pg;
  final double pr;
  final double trend;
  final Color color;
  const _CatAnalysis(this.avg, this.pg, this.pr, this.trend, this.color);
}