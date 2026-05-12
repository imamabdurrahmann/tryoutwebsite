import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../../core/constants/app_constants.dart';
import '../../../core/theme/app_theme.dart';
import '../../../core/router/app_router.dart';
import '../../../providers/questions_provider.dart';
import '../../../data/sources/hive_source.dart';

class SplashScreen extends ConsumerStatefulWidget {
  const SplashScreen({super.key});

  @override
  ConsumerState<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends ConsumerState<SplashScreen>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _fadeAnimation;
  late Animation<double> _scaleAnimation;

  String _statusText = 'Menyiapkan ruang ujian...';

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: const Duration(milliseconds: 800),
      vsync: this,
    );

    _fadeAnimation = Tween<double>(begin: 0.0, end: 1.0).animate(
      CurvedAnimation(parent: _controller, curve: Curves.easeIn),
    );

    _scaleAnimation = Tween<double>(begin: 0.8, end: 1.0).animate(
      CurvedAnimation(parent: _controller, curve: Curves.elasticOut),
    );

    _controller.forward();
    _initialize();
  }

  Future<void> _initialize() async {
    try {
      // Step 1: Validate Hive cache — clear if stale (wrong question count)
      _updateStatus('Memverifikasi data soal...');
      await _validateHiveCache();

      // Step 2: Load questions (reads from JSON if Hive was cleared)
      _updateStatus('Memuat ${AppConstants.totalQuestionCount} soal...');
      final repo = ref.read(questionRepositoryProvider);
      final questions = await repo.getAllQuestions();
      _updateStatus('${questions.length} soal siap');

      // Step 3: Navigate to home
      await Future.delayed(const Duration(milliseconds: 300));

      if (mounted) {
        appRouter.go('/home');
      }
    } catch (e) {
      if (mounted) {
        appRouter.go('/home');
      }
    }
  }

  Future<void> _validateHiveCache() async {
    final hive = HiveSource();
    final cached = hive.getAllQuestions();
    final expected = AppConstants.totalQuestionCount;

    if (cached.isNotEmpty && cached.length != expected) {
      // Stale cache from previous build — clear it
      await hive.clearQuestions();
    }
  }

  void _updateStatus(String text) {
    if (mounted) setState(() => _statusText = text);
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.primaryRed,
      body: Center(
        child: FadeTransition(
          opacity: _fadeAnimation,
          child: ScaleTransition(
            scale: _scaleAnimation,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                // Logo container
                Container(
                  width: 120,
                  height: 120,
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(28),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black.withAlpha(40),
                        blurRadius: 24,
                        offset: const Offset(0, 8),
                      ),
                    ],
                  ),
                  child: const Center(
                    child: Icon(
                      Icons.quiz_outlined,
                      color: AppTheme.primaryRed,
                      size: 64,
                    ),
                  ),
                ),
                const SizedBox(height: 24),

                // App name
                const Text(
                  'TryOutCPNS',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 28,
                    fontWeight: FontWeight.bold,
                    letterSpacing: 1,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  'Persiapan SKD 2024',
                  style: TextStyle(
                    color: Colors.white.withAlpha(180),
                    fontSize: 14,
                    fontWeight: FontWeight.w400,
                  ),
                ),
                const SizedBox(height: 48),

                // Loading indicator
                SizedBox(
                  width: 48,
                  height: 48,
                  child: CircularProgressIndicator(
                    color: Colors.white.withAlpha(200),
                    strokeWidth: 3,
                  ),
                ),
                const SizedBox(height: 20),

                // Status text — shows real-time count
                AnimatedSwitcher(
                  duration: const Duration(milliseconds: 300),
                  child: Text(
                    _statusText,
                    key: ValueKey(_statusText),
                    style: TextStyle(
                      color: Colors.white.withAlpha(180),
                      fontSize: 13,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}