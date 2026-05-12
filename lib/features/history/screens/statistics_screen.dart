import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:fl_chart/fl_chart.dart';
import 'package:intl/intl.dart';
import '../../../core/theme/app_theme.dart';
import '../../../providers/statistics_provider.dart';

class StatisticsScreen extends ConsumerWidget {
  const StatisticsScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final statsState = ref.watch(statisticsProvider);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Statistik'),
        actions: [
          IconButton(
            icon: const Icon(Icons.refresh),
            onPressed: () {
              ref.read(statisticsProvider.notifier).loadStatistics();
            },
          ),
        ],
      ),
      body: statsState.isLoading
          ? const Center(child: CircularProgressIndicator())
          : statsState.error != null
              ? Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(Icons.error_outline, size: 48, color: Colors.grey.shade400),
                      const SizedBox(height: 16),
                      Text('Error loading statistics',
                          style: TextStyle(color: Colors.grey.shade600)),
                      const SizedBox(height: 8),
                      ElevatedButton(
                        onPressed: () {
                          ref.read(statisticsProvider.notifier).loadStatistics();
                        },
                        child: const Text('Retry'),
                      ),
                    ],
                  ),
                )
              : statsState.sessions.isEmpty
                  ? _EmptyState()
                  : _StatisticsContent(statsState: statsState),
    );
  }
}

class _EmptyState extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(Icons.bar_chart, size: 80, color: Colors.grey.shade300),
          const SizedBox(height: 16),
          Text(
            'Belum ada data statistik',
            style: TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.bold,
              color: Colors.grey.shade600,
            ),
          ),
          const SizedBox(height: 8),
          Text(
            'Selesaikan try out untuk melihat statistik',
            style: TextStyle(color: Colors.grey.shade500),
          ),
        ],
      ),
    );
  }
}

class _StatisticsContent extends StatelessWidget {
  final StatisticsState statsState;

  const _StatisticsContent({required this.statsState});

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Overall Stats Card
          _OverallStatsCard(stats: statsState.overallStats),
          const SizedBox(height: 20),

          // Accuracy by Category Chart
          _AccuracyByCategorySection(categories: statsState.categoryAccuracy),
          const SizedBox(height: 20),

          // Trend Chart
          if (statsState.trendData.length > 1) ...[
            _TrendChartSection(trendData: statsState.trendData),
            const SizedBox(height: 20),
          ],

          // Weak Areas
          if (statsState.weakAreas.isNotEmpty) ...[
            _WeakAreasSection(weakAreas: statsState.weakAreas),
            const SizedBox(height: 20),
          ],

          // Strong Areas
          if (statsState.strongAreas.isNotEmpty) ...[
            _StrongAreasSection(strongAreas: statsState.strongAreas),
            const SizedBox(height: 20),
          ],

          // Improvement Trend Summary
          _ImprovementTrendSection(trendData: statsState.trendData),
        ],
      ),
    );
  }
}

class _OverallStatsCard extends StatelessWidget {
  final OverallStats stats;

  const _OverallStatsCard({required this.stats});

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 2,
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(Icons.analytics, color: AppTheme.primaryRed, size: 24),
                const SizedBox(width: 8),
                Text(
                  'Ringkasan Keseluruhan',
                  style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                ),
              ],
            ),
            const SizedBox(height: 20),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                _StatItem(
                  icon: Icons.play_circle_outline,
                  label: 'Total Sesi',
                  value: '${stats.totalSessions}',
                  color: AppTheme.secondaryBlue,
                ),
                _StatItem(
                  icon: Icons.check_circle_outline,
                  label: 'Lulus',
                  value: '${stats.passedSessions}',
                  color: AppTheme.successGreen,
                ),
                _StatItem(
                  icon: Icons.trending_up,
                  label: 'Rata-rata',
                  value: '${stats.averageScore.toStringAsFixed(0)}',
                  color: AppTheme.warningOrange,
                ),
                _StatItem(
                  icon: Icons.emoji_events,
                  label: 'Terbaik',
                  value: '${stats.bestScore}',
                  color: AppTheme.primaryRed,
                ),
              ],
            ),
            const SizedBox(height: 16),
            const Divider(),
            const SizedBox(height: 12),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                _SubStatItem(
                  label: 'Akurasi Keseluruhan',
                  value: '${stats.overallAccuracy.toStringAsFixed(1)}%',
                ),
                _SubStatItem(
                  label: 'Total Dijawab',
                  value: '${stats.totalQuestionsAnswered}',
                ),
                _SubStatItem(
                  label: 'Total Benar',
                  value: '${stats.totalCorrect}',
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

class _StatItem extends StatelessWidget {
  final IconData icon;
  final String label;
  final String value;
  final Color color;

  const _StatItem({
    required this.icon,
    required this.label,
    required this.value,
    required this.color,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Container(
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(
            color: color.withAlpha(26),
            shape: BoxShape.circle,
          ),
          child: Icon(icon, color: color, size: 28),
        ),
        const SizedBox(height: 8),
        Text(
          value,
          style: Theme.of(context).textTheme.titleLarge?.copyWith(
                fontWeight: FontWeight.bold,
                color: color,
              ),
        ),
        Text(
          label,
          style: TextStyle(
            fontSize: 12,
            color: Colors.grey.shade600,
          ),
        ),
      ],
    );
  }
}

class _SubStatItem extends StatelessWidget {
  final String label;
  final String value;

  const _SubStatItem({required this.label, required this.value});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text(
          value,
          style: const TextStyle(
            fontWeight: FontWeight.bold,
            fontSize: 14,
          ),
        ),
        Text(
          label,
          style: TextStyle(
            fontSize: 10,
            color: Colors.grey.shade600,
          ),
        ),
      ],
    );
  }
}

class _AccuracyByCategorySection extends StatelessWidget {
  final List<CategoryAccuracy> categories;

  const _AccuracyByCategorySection({required this.categories});

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 2,
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(Icons.pie_chart, color: AppTheme.primaryRed, size: 24),
                const SizedBox(width: 8),
                Text(
                  'Akurasi per Kategori',
                  style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                ),
              ],
            ),
            const SizedBox(height: 20),
            SizedBox(
              height: 200,
              child: BarChart(
                BarChartData(
                  alignment: BarChartAlignment.spaceAround,
                  maxY: 100,
                  barTouchData: BarTouchData(
                    touchTooltipData: BarTouchTooltipData(
                      getTooltipItem: (group, groupIndex, rod, rodIndex) {
                        final cat = categories[groupIndex];
                        return BarTooltipItem(
                          '${cat.category}\n${rod.toY.toStringAsFixed(1)}%',
                          const TextStyle(color: Colors.white, fontSize: 12),
                        );
                      },
                    ),
                  ),
                  titlesData: FlTitlesData(
                    show: true,
                    bottomTitles: AxisTitles(
                      sideTitles: SideTitles(
                        showTitles: true,
                        getTitlesWidget: (value, meta) {
                          final index = value.toInt();
                          if (index >= 0 && index < categories.length) {
                            return Padding(
                              padding: const EdgeInsets.only(top: 8),
                              child: Text(
                                categories[index].category,
                                style: const TextStyle(
                                  fontWeight: FontWeight.bold,
                                  fontSize: 12,
                                ),
                              ),
                            );
                          }
                          return const Text('');
                        },
                        reservedSize: 30,
                      ),
                    ),
                    leftTitles: AxisTitles(
                      sideTitles: SideTitles(
                        showTitles: true,
                        reservedSize: 40,
                        getTitlesWidget: (value, meta) {
                          return Text(
                            '${value.toInt()}%',
                            style: TextStyle(
                              fontSize: 10,
                              color: Colors.grey.shade600,
                            ),
                          );
                        },
                        interval: 25,
                      ),
                    ),
                    topTitles:
                        const AxisTitles(sideTitles: SideTitles(showTitles: false)),
                    rightTitles:
                        const AxisTitles(sideTitles: SideTitles(showTitles: false)),
                  ),
                  borderData: FlBorderData(show: false),
                  gridData: FlGridData(
                    show: true,
                    drawVerticalLine: false,
                    horizontalInterval: 25,
                    getDrawingHorizontalLine: (value) => FlLine(
                      color: Colors.grey.shade200,
                      strokeWidth: 1,
                    ),
                  ),
                  barGroups: categories.asMap().entries.map((entry) {
                    final index = entry.key;
                    final cat = entry.value;
                    final color = _getCategoryColor(cat.category);
                    return BarChartGroupData(
                      x: index,
                      barRods: [
                        BarChartRodData(
                          toY: cat.accuracy,
                          color: color,
                          width: 40,
                          borderRadius: const BorderRadius.only(
                            topLeft: Radius.circular(6),
                            topRight: Radius.circular(6),
                          ),
                          backDrawRodData: BackgroundBarChartRodData(
                            show: true,
                            toY: 100,
                            color: Colors.grey.shade200,
                          ),
                        ),
                      ],
                    );
                  }).toList(),
                ),
              ),
            ),
            const SizedBox(height: 16),
            // Legend with details
            ...categories.map((cat) => _CategoryAccuracyRow(
                  category: cat,
                  color: _getCategoryColor(cat.category),
                )),
          ],
        ),
      ),
    );
  }

  Color _getCategoryColor(String category) {
    switch (category) {
      case 'TWK':
        return AppTheme.secondaryBlue;
      case 'TIU':
        return AppTheme.warningOrange;
      case 'TKP':
        return AppTheme.successGreen;
      default:
        return AppTheme.primaryRed;
    }
  }
}

class _CategoryAccuracyRow extends StatelessWidget {
  final CategoryAccuracy category;
  final Color color;

  const _CategoryAccuracyRow({required this.category, required this.color});

  @override
  Widget build(BuildContext context) {
    final passingGrade = category.passingGrade;
    final isPassing = category.averageScore >= passingGrade;

    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: Row(
        children: [
          Container(
            width: 12,
            height: 12,
            decoration: BoxDecoration(
              color: color,
              shape: BoxShape.circle,
            ),
          ),
          const SizedBox(width: 8),
          SizedBox(
            width: 50,
            child: Text(
              category.category,
              style: const TextStyle(fontWeight: FontWeight.bold),
            ),
          ),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Text(
                      '${category.accuracy.toStringAsFixed(1)}%',
                      style: TextStyle(
                        fontWeight: FontWeight.bold,
                        color: color,
                      ),
                    ),
                    const SizedBox(width: 8),
                    Text(
                      '(${category.correct}/${category.total} benar)',
                      style: TextStyle(
                        fontSize: 11,
                        color: Colors.grey.shade600,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 4),
                ClipRRect(
                  borderRadius: BorderRadius.circular(4),
                  child: LinearProgressIndicator(
                    value: category.accuracy / 100,
                    backgroundColor: Colors.grey.shade200,
                    valueColor: AlwaysStoppedAnimation(color),
                    minHeight: 6,
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(width: 12),
          Column(
            crossAxisAlignment: CrossAxisAlignment.end,
            children: [
              Text(
                'Rata-rata: ${category.averageScore.toStringAsFixed(0)}',
                style: TextStyle(
                  fontSize: 11,
                  fontWeight: isPassing ? FontWeight.bold : FontWeight.normal,
                  color: isPassing ? AppTheme.successGreen : AppTheme.errorRed,
                ),
              ),
              Text(
                'PG: $passingGrade',
                style: TextStyle(
                  fontSize: 10,
                  color: Colors.grey.shade500,
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}

class _TrendChartSection extends StatelessWidget {
  final List<TrendPoint> trendData;

  const _TrendChartSection({required this.trendData});

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 2,
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(Icons.show_chart, color: AppTheme.primaryRed, size: 24),
                const SizedBox(width: 8),
                Text(
                  'Tren Perbaikan',
                  style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                ),
              ],
            ),
            const SizedBox(height: 20),
            SizedBox(
              height: 200,
              child: LineChart(
                LineChartData(
                  gridData: FlGridData(
                    show: true,
                    drawVerticalLine: false,
                    horizontalInterval: 100,
                    getDrawingHorizontalLine: (value) => FlLine(
                      color: Colors.grey.shade200,
                      strokeWidth: 1,
                    ),
                  ),
                  titlesData: FlTitlesData(
                    show: true,
                    bottomTitles: AxisTitles(
                      sideTitles: SideTitles(
                        showTitles: true,
                        reservedSize: 30,
                        getTitlesWidget: (value, meta) {
                          final index = value.toInt();
                          if (index >= 0 && index < trendData.length) {
                            return Padding(
                              padding: const EdgeInsets.only(top: 4),
                              child: Text(
                                DateFormat('dd/MM').format(trendData[index].date),
                                style: TextStyle(
                                  fontSize: 9,
                                  color: Colors.grey.shade600,
                                ),
                              ),
                            );
                          }
                          return const Text('');
                        },
                        interval: (trendData.length / 5).ceil().toDouble().clamp(1, 10),
                      ),
                    ),
                    leftTitles: AxisTitles(
                      sideTitles: SideTitles(
                        showTitles: true,
                        reservedSize: 40,
                        getTitlesWidget: (value, meta) {
                          return Text(
                            value.toInt().toString(),
                            style: TextStyle(
                              fontSize: 10,
                              color: Colors.grey.shade600,
                            ),
                          );
                        },
                        interval: 100,
                      ),
                    ),
                    topTitles:
                        const AxisTitles(sideTitles: SideTitles(showTitles: false)),
                    rightTitles:
                        const AxisTitles(sideTitles: SideTitles(showTitles: false)),
                  ),
                  borderData: FlBorderData(show: false),
                  minX: 0,
                  maxX: (trendData.length - 1).toDouble(),
                  minY: 0,
                  maxY: 550,
                  lineBarsData: [
                    // Total Score Line
                    LineChartBarData(
                      spots: trendData.asMap().entries.map((e) {
                        return FlSpot(
                          e.key.toDouble(),
                          e.value.totalScore,
                        );
                      }).toList(),
                      isCurved: true,
                      color: AppTheme.primaryRed,
                      barWidth: 3,
                      dotData: FlDotData(
                        show: true,
                        getDotPainter: (spot, percent, barData, index) {
                          return FlDotCirclePainter(
                            radius: 4,
                            color: trendData[index].passed
                                ? AppTheme.successGreen
                                : AppTheme.errorRed,
                            strokeWidth: 2,
                            strokeColor: Colors.white,
                          );
                        },
                      ),
                      belowBarData: BarAreaData(
                        show: true,
                        color: AppTheme.primaryRed.withAlpha(26),
                      ),
                    ),
                  ],
                  lineTouchData: LineTouchData(
                    touchTooltipData: LineTouchTooltipData(
                      getTooltipItems: (touchedSpots) {
                        return touchedSpots.map((spot) {
                          final index = spot.x.toInt();
                          final data = trendData[index];
                          return LineTooltipItem(
                            'Skor: ${spot.y.toInt()}\n${DateFormat('dd MMM').format(data.date)}\n${data.passed ? "Lulus" : "Tidak Lulus"}',
                            const TextStyle(color: Colors.white, fontSize: 12),
                          );
                        }).toList();
                      },
                    ),
                  ),
                ),
              ),
            ),
            const SizedBox(height: 12),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                _buildLegendItem(AppTheme.primaryRed, 'Total Skor'),
                const SizedBox(width: 20),
                _buildLegendItem(AppTheme.successGreen, 'Lulus'),
                const SizedBox(width: 20),
                _buildLegendItem(AppTheme.errorRed, 'Tidak Lulus'),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildLegendItem(Color color, String label) {
    return Row(
      children: [
        Container(
          width: 12,
          height: 12,
          decoration: BoxDecoration(
            color: color,
            shape: BoxShape.circle,
          ),
        ),
        const SizedBox(width: 4),
        Text(label, style: const TextStyle(fontSize: 11, color: Colors.grey)),
      ],
    );
  }
}

class _WeakAreasSection extends StatelessWidget {
  final List<SubcategoryStat> weakAreas;

  const _WeakAreasSection({required this.weakAreas});

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 2,
      color: AppTheme.errorRed.withAlpha(8),
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(Icons.warning_amber, color: AppTheme.errorRed, size: 24),
                const SizedBox(width: 8),
                Text(
                  'Area Lemah',
                  style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                        color: AppTheme.errorRed,
                      ),
                ),
              ],
            ),
            const SizedBox(height: 4),
            Text(
              'Perlu lebih banyak latihan',
              style: TextStyle(
                fontSize: 12,
                color: Colors.grey.shade600,
              ),
            ),
            const SizedBox(height: 16),
            ...weakAreas.take(5).map((area) => _AreaItem(
                  area: area,
                  isWeak: true,
                )),
          ],
        ),
      ),
    );
  }
}

class _StrongAreasSection extends StatelessWidget {
  final List<SubcategoryStat> strongAreas;

  const _StrongAreasSection({required this.strongAreas});

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 2,
      color: AppTheme.successGreen.withAlpha(8),
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(Icons.check_circle, color: AppTheme.successGreen, size: 24),
                const SizedBox(width: 8),
                Text(
                  'Area Kuat',
                  style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                        color: AppTheme.successGreen,
                      ),
                ),
              ],
            ),
            const SizedBox(height: 4),
            Text(
              'Pertahankan performa ini',
              style: TextStyle(
                fontSize: 12,
                color: Colors.grey.shade600,
              ),
            ),
            const SizedBox(height: 16),
            ...strongAreas.take(5).map((area) => _AreaItem(
                  area: area,
                  isWeak: false,
                )),
          ],
        ),
      ),
    );
  }
}

class _AreaItem extends StatelessWidget {
  final SubcategoryStat area;
  final bool isWeak;

  const _AreaItem({required this.area, required this.isWeak});

  @override
  Widget build(BuildContext context) {
    final color = isWeak ? AppTheme.errorRed : AppTheme.successGreen;

    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 6),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
            decoration: BoxDecoration(
              color: color.withAlpha(26),
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: color.withAlpha(51)),
            ),
            child: Text(
              area.category,
              style: TextStyle(
                fontWeight: FontWeight.bold,
                color: color,
                fontSize: 12,
              ),
            ),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  area.displayName,
                  style: const TextStyle(fontWeight: FontWeight.w500),
                ),
                const SizedBox(height: 4),
                ClipRRect(
                  borderRadius: BorderRadius.circular(4),
                  child: LinearProgressIndicator(
                    value: area.accuracy / 100,
                    backgroundColor: Colors.grey.shade200,
                    valueColor: AlwaysStoppedAnimation(color),
                    minHeight: 6,
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(width: 12),
          Column(
            crossAxisAlignment: CrossAxisAlignment.end,
            children: [
              Text(
                '${area.accuracy.toStringAsFixed(1)}%',
                style: TextStyle(
                  fontWeight: FontWeight.bold,
                  color: color,
                ),
              ),
              Text(
                '${area.correct}/${area.total}',
                style: TextStyle(
                  fontSize: 10,
                  color: Colors.grey.shade600,
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}

class _ImprovementTrendSection extends StatelessWidget {
  final List<TrendPoint> trendData;

  const _ImprovementTrendSection({required this.trendData});

  @override
  Widget build(BuildContext context) {
    if (trendData.length < 2) {
      return Card(
        elevation: 2,
        child: Padding(
          padding: const EdgeInsets.all(20),
          child: Column(
            children: [
              Icon(Icons.trending_up, size: 40, color: Colors.grey.shade400),
              const SizedBox(height: 8),
              Text(
                'Selesaikan minimal 2 sesi try out untuk melihat tren perbaikan',
                style: TextStyle(color: Colors.grey.shade600),
                textAlign: TextAlign.center,
              ),
            ],
          ),
        ),
      );
    }

    final recent = trendData.last;
    final older = trendData[trendData.length - 2];
    final scoreChange = recent.totalScore - older.totalScore;
    final isImproving = scoreChange > 0;
    final changeColor = isImproving ? AppTheme.successGreen : AppTheme.errorRed;

    return Card(
      elevation: 2,
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(
                  isImproving ? Icons.trending_up : Icons.trending_down,
                  color: changeColor,
                  size: 24,
                ),
                const SizedBox(width: 8),
                Text(
                  'Perbandingan Sesi Terakhir',
                  style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                ),
              ],
            ),
            const SizedBox(height: 16),
            Row(
              children: [
                Expanded(
                  child: _ComparisonCard(
                    label: 'Sesi Terakhir',
                    score: recent.totalScore.toInt(),
                    date: recent.date,
                    passed: recent.passed,
                  ),
                ),
                const SizedBox(width: 12),
                Container(
                  padding: const EdgeInsets.all(8),
                  child: Icon(
                    isImproving ? Icons.arrow_forward : Icons.arrow_back,
                    color: changeColor,
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: _ComparisonCard(
                    label: 'Sesi Sebelumnya',
                    score: older.totalScore.toInt(),
                    date: older.date,
                    passed: older.passed,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 16),
            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: changeColor.withAlpha(20),
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: changeColor.withAlpha(51)),
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(
                    isImproving ? Icons.arrow_upward : Icons.arrow_downward,
                    color: changeColor,
                    size: 20,
                  ),
                  const SizedBox(width: 8),
                  Text(
                    '${isImproving ? '+' : ''}${scoreChange.toInt()} poin',
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 16,
                      color: changeColor,
                    ),
                  ),
                  const SizedBox(width: 8),
                  Text(
                    isImproving ? 'Membaik!' : 'Menurun',
                    style: TextStyle(
                      color: changeColor,
                      fontSize: 12,
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _ComparisonCard extends StatelessWidget {
  final String label;
  final int score;
  final DateTime date;
  final bool passed;

  const _ComparisonCard({
    required this.label,
    required this.score,
    required this.date,
    required this.passed,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: Colors.grey.shade100,
        borderRadius: BorderRadius.circular(12),
      ),
      child: Column(
        children: [
          Text(
            label,
            style: TextStyle(
              fontSize: 11,
              color: Colors.grey.shade600,
            ),
          ),
          const SizedBox(height: 8),
          Text(
            '$score',
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 24,
              color: passed ? AppTheme.successGreen : AppTheme.errorRed,
            ),
          ),
          const SizedBox(height: 4),
          Text(
            DateFormat('dd MMM yyyy').format(date),
            style: TextStyle(
              fontSize: 10,
              color: Colors.grey.shade500,
            ),
          ),
          const SizedBox(height: 4),
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
            decoration: BoxDecoration(
              color: passed
                  ? AppTheme.successGreen.withAlpha(26)
                  : AppTheme.errorRed.withAlpha(26),
              borderRadius: BorderRadius.circular(10),
            ),
            child: Text(
              passed ? 'LULUS' : 'TL',
              style: TextStyle(
                fontSize: 10,
                fontWeight: FontWeight.bold,
                color: passed ? AppTheme.successGreen : AppTheme.errorRed,
              ),
            ),
          ),
        ],
      ),
    );
  }
}
