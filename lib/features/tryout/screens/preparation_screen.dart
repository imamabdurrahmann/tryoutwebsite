import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import '../../../core/models/package_metadata.dart';
import '../../../core/theme/app_theme.dart';
import '../../../providers/package_metadata_provider.dart';

/// PreparationScreen — countdown 3-2-1-GO sebelum exam starts.
/// Di-trigger sebelum masuk TryoutScreen.
///
/// Gunakan `packageMetadataProvider` sebagai single source of truth
/// untuk title, subtitle, jumlah soal, dan durasi. Tidak ada hardcode di widget tree.
class PreparationScreen extends ConsumerWidget {
  final String packageType;
  final VoidCallback onShowExitConfirmation;

  const PreparationScreen({
    super.key,
    required this.packageType,
    required this.onShowExitConfirmation,
  });

  void _showExitConfirmation(BuildContext context) {
    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Batalkan Persiapan?'),
        content: const Text('Kamu belum memulai try out.'),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx),
            child: const Text('Lanjut'),
          ),
          TextButton(
            onPressed: () {
              Navigator.pop(ctx);
              context.go('/home');
            },
            child: const Text('Batalkan'),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    // ===== DATA DRIVEN: metadata dari repository =====
    final meta = ref.watch(packageMetadataProvider(packageType));

    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, result) {
        if (!didPop) _showExitConfirmation(context);
      },
      child: Scaffold(
        backgroundColor: Theme.of(context).scaffoldBackgroundColor,
        appBar: AppBar(
          title: const Text('Persiapan'),
          leading: IconButton(
            icon: const Icon(Icons.close),
            onPressed: () => _showExitConfirmation(context),
          ),
          automaticallyImplyLeading: false,
        ),
        body: SafeArea(
          child: _PreparationContent(
            packageType: packageType,
            meta: meta,
          ),
        ),
      ),
    );
  }
}

/// Konten preparation (agreement + countdown overlay).
/// Dijadikan widget terpisah agar bisa di-split antara state agreement vs countdown.
class _PreparationContent extends ConsumerStatefulWidget {
  final String packageType;
  final PackageMetadata meta;

  const _PreparationContent({
    required this.packageType,
    required this.meta,
  });

  @override
  ConsumerState<_PreparationContent> createState() =>
      _PreparationContentState();
}

class _PreparationContentState extends ConsumerState<_PreparationContent>
    with SingleTickerProviderStateMixin {
  bool _agreed = false;
  bool _countdownStarted = false;
  int _countdown = 3;
  late AnimationController _animController;
  late Animation<double> _scaleAnimation;

  @override
  void initState() {
    super.initState();
    _animController = AnimationController(
      duration: const Duration(milliseconds: 800),
      vsync: this,
    );
    _scaleAnimation = Tween<double>(begin: 2.0, end: 1.0).animate(
      CurvedAnimation(parent: _animController, curve: Curves.easeOut),
    );
  }

  @override
  void dispose() {
    _animController.dispose();
    super.dispose();
  }

  void _startCountdown() async {
    if (_countdownStarted) return;
    setState(() => _countdownStarted = true);

    for (int i = 3; i >= 0; i--) {
      if (!mounted) return;
      setState(() => _countdown = i);
      _animController.reset();
      _animController.forward();
      await Future.delayed(Duration(milliseconds: i == 0 ? 800 : 1000));
    }

    if (mounted) {
      context.go('/tryout/${widget.packageType}');
    }
  }

  @override
  Widget build(BuildContext context) {
    if (_countdownStarted) {
      return _CountdownOverlay(
        meta: widget.meta,
        countdown: _countdown,
        animController: _animController,
        scaleAnimation: _scaleAnimation,
      );
    }
    return _buildPreparationContent(context);
  }

  Widget _buildPreparationContent(BuildContext context) {
    final meta = widget.meta;

    return Center(
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 900),
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(20),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // ===== Info Card — semua data dari metadata =====
              Container(
                width: double.infinity,
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(
              color: Theme.of(context).cardColor,
              borderRadius: BorderRadius.circular(16),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withAlpha(10),
                  blurRadius: 8,
                  offset: const Offset(0, 2),
                ),
              ],
            ),
            child: Column(
              children: [
                Container(
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: AppTheme.primaryRed.withAlpha(15),
                    shape: BoxShape.circle,
                  ),
                  child: Icon(
                    meta.isFull
                        ? Icons.assignment_turned_in
                        : meta.isTwk
                            ? Icons.balance
                            : meta.isTiu
                                ? Icons.calculate
                                : Icons.psychology,
                    color: AppTheme.primaryRed,
                    size: 40,
                  ),
                ),
                const SizedBox(height: 16),
                // ===== JUDUL: Title (Subtitle) =====
                Text(
                  '${meta.title} (${meta.subtitle})',
                  style: const TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                  ),
                  textAlign: TextAlign.center,
                ),
                const SizedBox(height: 8),
                // ===== RINGKASAN: X Soal • Y Menit =====
                Text(
                  '${meta.totalQuestions} Soal • ${meta.durationMinutes} Menit',
                  style: TextStyle(
                    fontSize: 14,
                    color: Colors.grey.shade600,
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 24),

          // Tata Tertib
          const Text(
            'Tata Tertib',
            style: TextStyle(
              fontSize: 16,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 12),
          ...List.generate(_tatibList.length, (i) => _buildTatibItem(i)),
          const SizedBox(height: 20),

          // Agreement Checkbox
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: Theme.of(context).cardColor,
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: Colors.grey.shade300),
            ),
            child: Row(
              children: [
                Checkbox(
                  value: _agreed,
                  activeColor: AppTheme.primaryRed,
                  onChanged: (v) => setState(() => _agreed = v ?? false),
                ),
                Expanded(
                  child: Text(
                    'Saya telah membaca dan memahami tata tertib di atas',
                    style: Theme.of(context).textTheme.bodyMedium,
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 24),

          // Start Button
          SizedBox(
            width: double.infinity,
            child: ElevatedButton(
              onPressed: _agreed ? _startCountdown : null,
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 16),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
              ),
              child: const Text(
                'MULAI TRY OUT',
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
            ),
          ),
          const SizedBox(height: 12),
          if (!_agreed)
            Center(
              child: Text(
                'Centang persetujuan untuk memulai',
                style: TextStyle(
                  fontSize: 12,
                  color: Colors.grey.shade500,
                ),
              ),
            ),
        ],
      ),
    ),
    ),
    );
  }

  static const List<Map<String, String>> _tatibList = [
    {
      'icon': '1',
      'title': 'Waktu berjalan otomatis',
      'desc': 'Timer dimulai saat kamu memasuki layar soal. Tidak bisa dijeda.',
    },
    {
      'icon': '2',
      'title': 'Jangan keluar aplikasi',
      'desc': 'Keluar dari aplikasi berarti kamu kehilangan progres try out.',
    },
    {
      'icon': '3',
      'title': 'Jawaban tersimpan otomatis',
      'desc': 'Setiap jawaban yang dipilih langsung tersimpan di perangkatmu.',
    },
    {
      'icon': '4',
      'title': 'Tanda soal ragu-ragu',
      'desc': 'Gunakan tombol bendera untuk menandai soal yang ingin di-review.',
    },
    {
      'icon': '5',
      'title': 'Timer habis = auto submit',
      'desc': 'Try out akan dikirim secara otomatis ketika waktu habis.',
    },
  ];

  Widget _buildTatibItem(int index) {
    final item = _tatibList[index];
    return Padding(
      padding: const EdgeInsets.only(bottom: 10),
      child: Container(
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: Theme.of(context).cardColor,
          borderRadius: BorderRadius.circular(10),
          border: Border.all(color: Colors.grey.shade200),
        ),
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              width: 28,
              height: 28,
              decoration: BoxDecoration(
                color: AppTheme.primaryRed.withAlpha(15),
                shape: BoxShape.circle,
              ),
              child: Center(
                child: Text(
                  item['icon']!,
                  style: const TextStyle(
                    color: AppTheme.primaryRed,
                    fontWeight: FontWeight.bold,
                    fontSize: 13,
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
                    item['title']!,
                    style: const TextStyle(fontWeight: FontWeight.w600, fontSize: 13),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    item['desc']!,
                    style: TextStyle(fontSize: 12, color: Colors.grey.shade600),
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

/// Countdown overlay — menampilkan metadata paket di bawah animasi GO.
class _CountdownOverlay extends StatelessWidget {
  final PackageMetadata meta;
  final int countdown;
  final AnimationController animController;
  final Animation<double> scaleAnimation;

  const _CountdownOverlay({
    required this.meta,
    required this.countdown,
    required this.animController,
    required this.scaleAnimation,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Theme.of(context).scaffoldBackgroundColor,
      child: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            ScaleTransition(
              scale: scaleAnimation,
              child: Container(
                width: 160,
                height: 160,
                decoration: BoxDecoration(
                  color: Colors.white,
                  shape: BoxShape.circle,
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black.withAlpha(40),
                      blurRadius: 30,
                      spreadRadius: 5,
                    ),
                  ],
                ),
                child: Center(
                  child: Text(
                    countdown == 0 ? 'GO!' : '$countdown',
                    style: TextStyle(
                      fontSize: countdown == 0 ? 56 : 72,
                      fontWeight: FontWeight.bold,
                      color: AppTheme.primaryRed,
                    ),
                  ),
                ),
              ),
            ),
            const SizedBox(height: 32),
            const Text(
              'Bersiap untuk Memulai!',
              style: TextStyle(
                color: Colors.white,
                fontSize: 22,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 8),
            // ===== LABEL PAKET di countdown overlay =====
            Text(
              '${meta.title} (${meta.subtitle})',
              style: TextStyle(
                color: Colors.white.withAlpha(200),
                fontSize: 16,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
