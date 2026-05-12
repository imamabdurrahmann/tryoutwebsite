import 'dart:io';
import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import '../../../core/theme/app_theme.dart';
import '../../../core/utils/app_utils.dart';
import '../../../core/utils/auto_save_service.dart';
import '../../../core/models/motivation_quote.dart';
import '../../../providers/tryout_provider.dart';
import '../../../providers/user_provider.dart';
import '../../../providers/questions_provider.dart';
import '../widgets/package_card.dart';

bool get _isDesktopDevice {
  if (kIsWeb) return false;
  return Platform.isWindows || Platform.isLinux || Platform.isMacOS;
}

class HomeScreen extends ConsumerWidget {
  const HomeScreen({super.key});

  bool _isDesktopScreen(BuildContext context) {
    return MediaQuery.of(context).size.width > 900;
  }

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final statsAsync = ref.watch(statsProvider);
    final theme = Theme.of(context);
    final quote = MotivationQuote.getRandom();
    final screenWidth = MediaQuery.of(context).size.width;
    final isWideScreen = screenWidth > 900;
    final isMediumScreen = screenWidth > 600;

    return Scaffold(
      backgroundColor: theme.scaffoldBackgroundColor,
      body: SafeArea(
        child: RefreshIndicator(
          onRefresh: () async {
            ref.invalidate(statsProvider);
          },
          child: Center(
            child: ConstrainedBox(
              constraints: BoxConstraints(
                maxWidth: isWideScreen ? 1200 : (isMediumScreen ? 800 : 500),
              ),
              child: CustomScrollView(
            slivers: [
              // ===== App Bar =====
              SliverAppBar(
                floating: true,
                backgroundColor: theme.scaffoldBackgroundColor,
                elevation: 0,
                toolbarHeight: 56,
                title: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      quote.headline,
                      style: theme.textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                        color: AppTheme.primaryRed,
                      ),
                    ),
                    Text(
                      quote.subHeadline,
                      style: theme.textTheme.bodySmall?.copyWith(
                        color: Colors.grey.shade600,
                        fontSize: 11,
                      ),
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                    ),
                  ],
                ),
                actions: [
                  IconButton(
                    icon: Icon(
                      theme.brightness == Brightness.dark
                          ? Icons.light_mode
                          : Icons.dark_mode,
                      color: AppTheme.primaryRed,
                    ),
                    onPressed: () {
                      final userSettingsNotifier = ref.read(userSettingsProvider.notifier);
                      final current = ref.read(userSettingsProvider);
                      userSettingsNotifier.setDarkMode(!current.darkMode);
                    },
                    tooltip: 'Ganti Tema',
                  ),
                ],
              ),

              // ===== Konten Utama =====
              SliverPadding(
                padding: EdgeInsets.symmetric(horizontal: isWideScreen ? 24 : 16),
                sliver: SliverList(
                  delegate: SliverChildListDelegate([
                    const SizedBox(height: 4),

                    // Wide Screen (>900px): Passing Grade + Statistik horizontal
                    if (isWideScreen)
                      Row(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Expanded(
                            flex: 3,
                            child: _buildPassingGradeBanner(context),
                          ),
                          const SizedBox(width: 12),
                          Expanded(
                            flex: 2,
                            child: statsAsync.when(
                              data: (stats) => _buildStatsCard(context, stats),
                              loading: () => _buildStatsSkeleton(context),
                              error: (_, __) =>
                                  _buildStatsCard(context, {'totalSessions': 0, 'streak': 0}),
                            ),
                          ),
                        ],
                      )
                    else ...[
                      // Narrow/Medium Screen: stacked
                      _buildPassingGradeBanner(context),
                      const SizedBox(height: 16),
                      statsAsync.when(
                        data: (stats) => _buildStatsCard(context, stats),
                        loading: () => _buildStatsSkeleton(context),
                        error: (_, __) =>
                            _buildStatsCard(context, {'totalSessions': 0, 'streak': 0}),
                      ),
                    ],
                    const SizedBox(height: 16),

                    // Resume Tryout Banner
                    _buildResumeBanner(context, ref),

                    // Section Title
                    Text(
                      'Paket Try Out',
                      style: theme.textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(height: 10),

                    // Grid Paket - responsive based on screen width
                    GridView.count(
                      shrinkWrap: true,
                      physics: const NeverScrollableScrollPhysics(),
                      crossAxisCount: isWideScreen ? 4 : (isMediumScreen ? 3 : 2),
                      mainAxisSpacing: 10,
                      crossAxisSpacing: 10,
                      childAspectRatio: isWideScreen ? 1.1 : 0.92,
                      children: [
                        PackageCard(
                          title: 'Try Out\nLengkap',
                          subtitle: '',
                          icon: Icons.assignment_turned_in,
                          color: AppTheme.primaryRed,
                          onTap: () => context.push('/package-selection/TOL'),
                          largeIcon: true,
                        ),
                        PackageCard(
                          title: 'Latihan\nTWK',
                          subtitle: '',
                          icon: Icons.balance,
                          color: AppTheme.secondaryBlue,
                          onTap: () => context.push('/package-selection/TWK'),
                        ),
                        PackageCard(
                          title: 'Latihan\nTIU',
                          subtitle: '',
                          icon: Icons.calculate,
                          color: AppTheme.warningOrange,
                          onTap: () => context.push('/package-selection/TIU'),
                        ),
                        PackageCard(
                          title: 'Latihan\nTKP',
                          subtitle: '',
                          icon: Icons.psychology,
                          color: AppTheme.successGreen,
                          onTap: () => context.push('/package-selection/TKP'),
                        ),
                      ],
                    ),
                    const SizedBox(height: 14),

                    // Tombol Latihan Per Subtopik
                    SizedBox(
                      width: double.infinity,
                      child: OutlinedButton.icon(
                        onPressed: () => context.push('/practice'),
                        icon: const Icon(Icons.school),
                        label: const Text('Latihan Per Subtopik'),
                        style: OutlinedButton.styleFrom(
                          padding: const EdgeInsets.symmetric(vertical: 12),
                          side: const BorderSide(
                            color: AppTheme.primaryRed,
                            width: 2,
                          ),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(12),
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(height: 16),

                    // Credit Banner
                    AppUtils.buildCreditBanner(context),

                    const SizedBox(height: 24),
                  ]),
                ),
              ),
            ],
          ),
        ),
        ),
        ),
      ),
    );
  }

  Widget _buildPassingGradeBanner(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
      decoration: BoxDecoration(
        gradient: const LinearGradient(
          colors: [AppTheme.primaryRed, AppTheme.primaryRedDark],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(12),
        boxShadow: [
          BoxShadow(
            color: AppTheme.primaryRed.withAlpha(60),
            blurRadius: 12,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              const Icon(Icons.verified, color: Colors.white, size: 16),
              const SizedBox(width: 6),
              const Expanded(
                child: Text(
                  'Passing Grade Resmi SKD 2024',
                  style: TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                    fontSize: 12,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 10),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              _buildGradeItem('TWK', '≥ 65'),
              _divider(),
              _buildGradeItem('TIU', '≥ 80'),
              _divider(),
              _buildGradeItem('TKP', '≥ 166'),
            ],
          ),
        ],
      ),
    );
  }

  Widget _divider() {
    return Container(
      width: 1,
      height: 28,
      color: Colors.white24,
    );
  }

  Widget _buildGradeItem(String label, String value) {
    return Column(
      children: [
        Text(
          label,
          style: const TextStyle(
            color: Colors.white70,
            fontSize: 11,
            fontWeight: FontWeight.w500,
          ),
        ),
        const SizedBox(height: 4),
        Text(
          value,
          style: const TextStyle(
            color: Colors.white,
            fontWeight: FontWeight.bold,
            fontSize: 15,
          ),
        ),
      ],
    );
  }

  Widget _buildStatsCard(BuildContext context, Map<String, dynamic> stats) {
    final totalSessions = stats['totalSessions'] ?? 0;
    final streak = stats['streak'] ?? 0;

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
      decoration: BoxDecoration(
        color: Theme.of(context).cardColor,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: Colors.grey.shade200),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withAlpha(12),
            blurRadius: 6,
            offset: const Offset(0, 2),
          ),
        ],
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        children: [
          _buildStatItem(
            context,
            Icons.assignment,
            '$totalSessions',
            'Total Sesi',
            AppTheme.primaryRed,
          ),
          Container(width: 1, height: 36, color: Colors.grey.shade300),
          _buildStatItem(
            context,
            Icons.local_fire_department,
            '$streak',
            'Hari Streak',
            AppTheme.warningOrange,
          ),
        ],
      ),
    );
  }

  Widget _buildStatItem(
    BuildContext context,
    IconData icon,
    String value,
    String label,
    Color color,
  ) {
    return Row(
      children: [
        Container(
          padding: const EdgeInsets.all(8),
          decoration: BoxDecoration(
            color: color.withAlpha(20),
            shape: BoxShape.circle,
          ),
          child: Icon(icon, color: color, size: 18),
        ),
        const SizedBox(width: 10),
        Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              value,
              style: Theme.of(context).textTheme.titleMedium?.copyWith(
                    fontWeight: FontWeight.bold,
                    color: color,
                  ),
            ),
            Text(
              label,
              style: Theme.of(context).textTheme.bodySmall?.copyWith(
                    color: Colors.grey.shade600,
                    fontSize: 11,
                  ),
            ),
          ],
        ),
      ],
    );
  }

  Widget _buildStatsSkeleton(BuildContext context) {
    return Container(
      height: 76,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Theme.of(context).cardColor,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.grey.shade200),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        children: [
          for (var i = 0; i < 2; i++) ...[
            Container(
              width: 36,
              height: 36,
              decoration: BoxDecoration(
                color: Colors.grey.shade300,
                shape: BoxShape.circle,
              ),
            ),
            const SizedBox(width: 12),
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: [
                Container(
                  width: 36,
                  height: 20,
                  color: Colors.grey.shade300,
                ),
                const SizedBox(height: 4),
                Container(
                  width: 60,
                  height: 12,
                  color: Colors.grey.shade200,
                ),
              ],
            ),
            if (i == 0) const SizedBox(width: 32),
          ],
        ],
      ),
    );
  }

  Widget _buildResumeBanner(BuildContext context, WidgetRef ref) {
    return FutureBuilder<Map<String, dynamic>?>(
      future: AutoSaveService.load(),
      builder: (context, snapshot) {
        if (!snapshot.hasData || snapshot.data == null) {
          return const SizedBox.shrink();
        }

        final data = snapshot.data!;
        final packageType = data['packageType'] ?? 'FULL';
        final answered = (data['answers'] as Map?)?.length ?? 0;
        final total = (data['questionIds'] as List?)?.length ?? 0;
        final remaining = data['remainingSeconds'] ?? 0;
        final mins = remaining ~/ 60;

        return Padding(
          padding: const EdgeInsets.only(bottom: 16),
          child: Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(
              gradient: LinearGradient(
                colors: [
                  AppTheme.warningOrange.withAlpha(25),
                  AppTheme.warningOrange.withAlpha(10),
                ],
              ),
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: AppTheme.warningOrange.withAlpha(60)),
            ),
            child: Row(
              children: [
                const Icon(Icons.restore, color: AppTheme.warningOrange, size: 28),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text(
                        'Tryout Belum Selesai',
                        style: TextStyle(
                          fontWeight: FontWeight.bold,
                          fontSize: 13,
                          color: AppTheme.warningOrange,
                        ),
                      ),
                      const SizedBox(height: 2),
                      Text(
                        '$packageType • $answered/$total dijawab • ${mins}m tersisa',
                        style: TextStyle(fontSize: 11, color: Colors.grey.shade700),
                      ),
                    ],
                  ),
                ),
                const SizedBox(width: 8),
                Column(
                  children: [
                    SizedBox(
                      height: 30,
                      child: ElevatedButton(
                        onPressed: () async {
                          final repo = ref.read(questionRepositoryProvider);
                          final allQ = await repo.getAllQuestions();
                          final notifier = ref.read(tryoutProvider.notifier);
                          final resumed = await notifier.resumeFromAutoSave(allQ);
                          if (resumed && context.mounted) {
                            context.push('/tryout/$packageType');
                          }
                        },
                        style: ElevatedButton.styleFrom(
                          padding: const EdgeInsets.symmetric(horizontal: 12),
                          backgroundColor: AppTheme.warningOrange,
                          textStyle: const TextStyle(fontSize: 11),
                        ),
                        child: const Text('Lanjutkan'),
                      ),
                    ),
                    const SizedBox(height: 4),
                    GestureDetector(
                      onTap: () async {
                        await AutoSaveService.clear();
                        ref.read(refreshTriggerProvider.notifier).state++;
                      },
                      child: Text(
                        'Hapus',
                        style: TextStyle(
                          fontSize: 10,
                          color: Colors.grey.shade500,
                          decoration: TextDecoration.underline,
                        ),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        );
      },
    );
  }
}
