import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import '../../../core/models/package_metadata.dart';
import '../../../core/theme/app_theme.dart';

/// PackageSelectionScreen — pilih Paket 1 atau Paket 2.
/// Semua metadata paket berasal dari PackageMetadataRepository (data-driven).
class PackageSelectionScreen extends ConsumerWidget {
  final String category;

  const PackageSelectionScreen({super.key, required this.category});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final theme = Theme.of(context);

    return Scaffold(
      backgroundColor: theme.scaffoldBackgroundColor,
      appBar: AppBar(
        title: Text(_getTitle()),
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: () => context.pop(),
        ),
      ),
      body: Center(
        child: ConstrainedBox(
          constraints: const BoxConstraints(maxWidth: 900),
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // ===== Header Deskriptif Dinamis =====
                _buildHeaderCard(context),
                const SizedBox(height: 24),

                // ===== Section Title =====
                Text(
                  'Pilih Paket',
                  style: theme.textTheme.titleMedium?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 14),

                // ===== Paket 1 & 2 Cards — data-driven =====
                ..._buildPackageCards(context),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildHeaderCard(BuildContext context) {
    final metaList = _getMetadataForCategory();
    if (metaList.isEmpty) return const SizedBox.shrink();

    final firstMeta = metaList.first;

    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [
            AppTheme.primaryRed.withAlpha(15),
            AppTheme.secondaryBlue.withAlpha(10),
          ],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: AppTheme.primaryRed.withAlpha(30),
        ),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: AppTheme.primaryRed.withAlpha(20),
              shape: BoxShape.circle,
            ),
            child: Icon(
              _getCategoryIcon(),
              color: AppTheme.primaryRed,
              size: 24,
            ),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  firstMeta.title,
                  style: Theme.of(context).textTheme.titleMedium?.copyWith(
                    fontWeight: FontWeight.bold,
                    color: AppTheme.primaryRed,
                  ),
                ),
                const SizedBox(height: 6),
                Text(
                  // ===== RINGKASAN DINAMIS =====
                  '${firstMeta.totalQuestions} Soal • ${firstMeta.durationMinutes} Menit',
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

  List<Widget> _buildPackageCards(BuildContext context) {
    final metaList = _getMetadataForCategory();
    return metaList.map((meta) {
      return Padding(
        padding: const EdgeInsets.only(bottom: 12),
        child: _buildPaketCard(context, meta: meta),
      );
    }).toList();
  }

  Widget _buildPaketCard(BuildContext context, {required PackageMetadata meta}) {
    final theme = Theme.of(context);
    final color = _getCategoryColor();
    final isDark = theme.brightness == Brightness.dark;

    return Card(
      elevation: 0,
      clipBehavior: Clip.antiAlias,
      shadowColor: color.withAlpha(60),
      child: InkWell(
        onTap: () => _navigateToPreparation(context, meta.packageId),
        splashColor: color.withAlpha(25),
        highlightColor: color.withAlpha(12),
        child: Container(
          padding: const EdgeInsets.all(20),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(16),
            gradient: LinearGradient(
              colors: isDark
                  ? [color.withAlpha(40), color.withAlpha(20)]
                  : [color.withAlpha(30), color.withAlpha(10)],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
            border: Border.all(
              color: color.withAlpha(isDark ? 50 : 40),
              width: 1,
            ),
          ),
          child: Row(
            children: [
              // Badge number dari subtitle paket
              _PaketBadge(
                paketNumber: meta.packageId.endsWith('_2') ? '2' : '1',
                color: color,
              ),
              const SizedBox(width: 16),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      meta.subtitle,
                      style: theme.textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                        color: color,
                      ),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      '${meta.totalQuestions} Soal • ${meta.durationMinutes} Menit',
                      style: theme.textTheme.bodySmall?.copyWith(
                        color: Colors.grey.shade600,
                      ),
                    ),
                  ],
                ),
              ),
              Icon(
                Icons.arrow_forward_ios,
                color: color.withAlpha(150),
                size: 18,
              ),
            ],
          ),
        ),
      ),
    );
  }

  void _navigateToPreparation(BuildContext context, String packageId) {
    final meta = PackageMetadataRepository.get(packageId);
    final color = _getCategoryColor();

    showDialog(
      context: context,
      builder: (dialogContext) => AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        title: Row(
          children: [
            Icon(Icons.timer, color: color),
            const SizedBox(width: 8),
            const Text('Mulai Try Out'),
          ],
        ),
        content: Text(
          // ===== PESAN DINAMIS dari metadata =====
          '${meta.title} (${meta.subtitle}): ${meta.totalQuestions} soal dalam ${meta.durationMinutes} menit.\nPastikan kamu memiliki waktu yang cukup.',
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(dialogContext),
            child: const Text('Batal'),
          ),
          ElevatedButton(
            onPressed: () {
              Navigator.pop(dialogContext);
              context.push('/prepare/$packageId');
            },
            style: ElevatedButton.styleFrom(backgroundColor: color),
            child: const Text('Mulai', style: TextStyle(color: Colors.white)),
          ),
        ],
      ),
    );
  }

  /// Ambil metadata paket untuk kategori saat ini.
  List<PackageMetadata> _getMetadataForCategory() {
    switch (category) {
      case 'TOL':
        return PackageMetadataRepository.getByBase('FULL');
      case 'TWK':
        return PackageMetadataRepository.getByBase('TWK_ONLY');
      case 'TIU':
        return PackageMetadataRepository.getByBase('TIU_ONLY');
      case 'TKP':
        return PackageMetadataRepository.getByBase('TKP_ONLY');
      default:
        return [];
    }
  }

  String _getTitle() {
    switch (category) {
      case 'TOL':
        return 'Try Out Lengkap';
      case 'TWK':
        return 'Latihan TWK';
      case 'TIU':
        return 'Latihan TIU';
      case 'TKP':
        return 'Latihan TKP';
      default:
        return 'Pilih Paket';
    }
  }

  IconData _getCategoryIcon() {
    switch (category) {
      case 'TOL':
        return Icons.assignment_turned_in;
      case 'TWK':
        return Icons.balance;
      case 'TIU':
        return Icons.calculate;
      case 'TKP':
        return Icons.psychology;
      default:
        return Icons.quiz;
    }
  }

  Color _getCategoryColor() {
    switch (category) {
      case 'TOL':
        return AppTheme.primaryRed;
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

/// Badge circular untuk nomor paket.
class _PaketBadge extends StatelessWidget {
  final String paketNumber;
  final Color color;

  const _PaketBadge({required this.paketNumber, required this.color});

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;

    return Container(
      width: 52,
      height: 52,
      decoration: BoxDecoration(
        color: color.withAlpha(isDark ? 50 : 30),
        shape: BoxShape.circle,
        boxShadow: [
          BoxShadow(
            color: color.withAlpha(30),
            blurRadius: 12,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Center(
        child: Text(
          paketNumber,
          style: TextStyle(
            color: color,
            fontWeight: FontWeight.bold,
            fontSize: 22,
          ),
        ),
      ),
    );
  }
}
