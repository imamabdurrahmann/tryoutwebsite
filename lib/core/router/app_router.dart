import 'dart:io';
import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../features/home/screens/home_screen.dart';
import '../../features/home/screens/splash_screen.dart';
import '../../features/home/screens/package_selection_screen.dart';
import '../../features/history/screens/history_screen.dart';
import '../../features/profile/screens/profile_screen.dart';
import '../../features/tryout/screens/tryout_screen.dart';
import '../../features/tryout/screens/preparation_screen.dart';
import '../../features/tryout/screens/review_screen.dart';
import '../../features/result/screens/result_screen.dart';
import '../../features/practice/screens/practice_screen.dart';

final GlobalKey<NavigatorState> _rootNavigatorKey = GlobalKey<NavigatorState>();
final GlobalKey<NavigatorState> _shellNavigatorKey = GlobalKey<NavigatorState>();

/// Key untuk BottomNavigationBar state di luar shell
final GlobalKey<NavigatorState> bottomNavKey = GlobalKey<NavigatorState>();

int _getShellIndex(String location) {
  if (location.startsWith('/home')) return 0;
  if (location.startsWith('/history')) return 1;
  if (location.startsWith('/profile')) return 2;
  return 0;
}

final GoRouter appRouter = GoRouter(
  navigatorKey: _rootNavigatorKey,
  initialLocation: '/',
  routes: [
    // ===== SPLASH SCREEN (initial route) =====
    GoRoute(
      path: '/',
      pageBuilder: (context, state) => CustomTransitionPage(
        key: state.pageKey,
        child: const SplashScreen(),
        transitionsBuilder: _fadeTransition,
      ),
    ),

    // ===== SHELL: Home + History + Profile dengan BottomNavigation =====
    ShellRoute(
      navigatorKey: _shellNavigatorKey,
      builder: (context, state, child) {
        return _ShellScaffold(
          key: bottomNavKey,
          location: state.uri.path,
          child: child,
        );
      },
      routes: [
        GoRoute(
          path: '/home',
          pageBuilder: (context, state) => CustomTransitionPage(
            key: state.pageKey,
            child: const HomeScreen(),
            transitionsBuilder: _fadeTransition,
          ),
        ),
        GoRoute(
          path: '/history',
          pageBuilder: (context, state) => CustomTransitionPage(
            key: state.pageKey,
            child: const HistoryScreen(),
            transitionsBuilder: _fadeTransition,
          ),
        ),
        GoRoute(
          path: '/profile',
          pageBuilder: (context, state) => CustomTransitionPage(
            key: state.pageKey,
            child: const ProfileScreen(),
            transitionsBuilder: _fadeTransition,
          ),
        ),
      ],
    ),

    // ===== FULL SCREEN: Package Selection (sub-menu) =====
    GoRoute(
      path: '/package-selection/:category',
      pageBuilder: (context, state) {
        final category = state.pathParameters['category'] ?? 'TOL';
        return CustomTransitionPage(
          key: state.pageKey,
          child: PackageSelectionScreen(category: category),
          transitionsBuilder: _slideTransition,
        );
      },
    ),

    // ===== FULL SCREEN: Preparation Screen (countdown before exam) =====
    GoRoute(
      path: '/prepare/:packageType',
      pageBuilder: (context, state) {
        final packageType = state.pathParameters['packageType'] ?? 'FULL';
        return CustomTransitionPage(
          key: state.pageKey,
          child: PreparationScreen(
            packageType: packageType,
            onShowExitConfirmation: () => context.go('/home'),
          ),
          transitionsBuilder: _slideTransition,
        );
      },
    ),

    // ===== FULL SCREEN: Tryout (tanpa BottomNavigation) =====
    GoRoute(
      path: '/tryout/:packageType',
      pageBuilder: (context, state) {
        final packageType = state.pathParameters['packageType'] ?? 'FULL';
        return CustomTransitionPage(
          key: state.pageKey,
          child: TryoutScreen(packageType: packageType),
          transitionsBuilder: _slideTransition,
        );
      },
    ),

    // ===== FULL SCREEN: Result (tanpa BottomNavigation) =====
    GoRoute(
      path: '/result/:sessionId',
      pageBuilder: (context, state) {
        final sessionId = state.pathParameters['sessionId'] ?? '';
        return CustomTransitionPage(
          key: state.pageKey,
          child: ResultScreen(sessionId: sessionId),
          transitionsBuilder: _fadeTransition,
        );
      },
    ),

    // ===== FULL SCREEN: Review (tanpa BottomNavigation) =====
    GoRoute(
      path: '/review/:sessionId',
      pageBuilder: (context, state) {
        final sessionId = state.pathParameters['sessionId'] ?? '';
        return CustomTransitionPage(
          key: state.pageKey,
          child: ReviewScreen(sessionId: sessionId),
          transitionsBuilder: _fadeTransition,
        );
      },
    ),

    // ===== FULL SCREEN: Practice (tanpa BottomNavigation) =====
    GoRoute(
      path: '/practice',
      pageBuilder: (context, state) => CustomTransitionPage(
        key: state.pageKey,
        child: const PracticeScreen(),
        transitionsBuilder: _slideTransition,
      ),
    ),
  ],
);

// ============================================================================
// SHELL SCAFFOLD — BottomNavigationBar dengan Navigator bersarang
// ============================================================================

class _ShellScaffold extends StatelessWidget {
  final Widget child;
  final String location;

  const _ShellScaffold({
    super.key,
    required this.child,
    required this.location,
  });

  bool get _isDesktop {
    if (kIsWeb) return false;
    return Platform.isWindows || Platform.isLinux || Platform.isMacOS;
  }

  @override
  Widget build(BuildContext context) {
    final selectedIndex = _getShellIndex(location);
    final screenWidth = MediaQuery.of(context).size.width;
    final isNarrowScreen = screenWidth < 600;

    // Desktop (non-web native): NavigationRail (sidebar kiri)
    if (_isDesktop) {
      return Scaffold(
        body: Row(
          children: [
            NavigationRail(
              selectedIndex: selectedIndex,
              onDestinationSelected: (index) => _onItemTapped(context, index),
              labelType: NavigationRailLabelType.all,
              backgroundColor: Theme.of(context).colorScheme.surface,
              leading: Padding(
                padding: const EdgeInsets.symmetric(vertical: 12),
                child: Column(
                  children: [
                    Icon(Icons.school, color: Theme.of(context).colorScheme.primary, size: 28),
                    const SizedBox(height: 4),
                    Text(
                      'CPNS',
                      style: TextStyle(
                        fontSize: 10,
                        fontWeight: FontWeight.bold,
                        color: Theme.of(context).colorScheme.primary,
                      ),
                    ),
                  ],
                ),
              ),
              destinations: const [
                NavigationRailDestination(
                  icon: Icon(Icons.home_outlined),
                  selectedIcon: Icon(Icons.home),
                  label: Text('Beranda'),
                ),
                NavigationRailDestination(
                  icon: Icon(Icons.history_outlined),
                  selectedIcon: Icon(Icons.history),
                  label: Text('Riwayat'),
                ),
                NavigationRailDestination(
                  icon: Icon(Icons.person_outlined),
                  selectedIcon: Icon(Icons.person),
                  label: Text('Profil'),
                ),
              ],
            ),
            const VerticalDivider(thickness: 1, width: 1),
            Expanded(child: child),
          ],
        ),
      );
    }

    // All mobile/small screens: Standard NavigationBar
    return Scaffold(
      body: child,
      bottomNavigationBar: NavigationBar(
        selectedIndex: selectedIndex,
        onDestinationSelected: (index) => _onItemTapped(context, index),
        destinations: const [
          NavigationDestination(
            icon: Icon(Icons.home_outlined),
            selectedIcon: Icon(Icons.home),
            label: 'Beranda',
          ),
          NavigationDestination(
            icon: Icon(Icons.history_outlined),
            selectedIcon: Icon(Icons.history),
            label: 'Riwayat',
          ),
          NavigationDestination(
            icon: Icon(Icons.person_outlined),
            selectedIcon: Icon(Icons.person),
            label: 'Profil',
          ),
        ],
      ),
    );
  }
          NavigationDestination(
            icon: Icon(Icons.home_outlined),
            selectedIcon: Icon(Icons.home),
            label: 'Beranda',
          ),
          NavigationDestination(
            icon: Icon(Icons.history_outlined),
            selectedIcon: Icon(Icons.history),
            label: 'Riwayat',
          ),
          NavigationDestination(
            icon: Icon(Icons.person_outlined),
            selectedIcon: Icon(Icons.person),
            label: 'Profil',
          ),
        ],
      ),
    );
  }

  void _onItemTapped(BuildContext context, int index) {
    switch (index) {
      case 0:
        context.go('/home');
        break;
      case 1:
        context.go('/history');
        break;
      case 2:
        context.go('/profile');
        break;
    }
  }
}

// ============================================================================
// TRANSISI
// ============================================================================

Widget _fadeTransition(
  BuildContext context,
  Animation<double> animation,
  Animation<double> secondaryAnimation,
  Widget child,
) {
  return FadeTransition(opacity: animation, child: child);
}

Widget _slideTransition(
  BuildContext context,
  Animation<double> animation,
  Animation<double> secondaryAnimation,
  Widget child,
) {
  return SlideTransition(
    position: Tween<Offset>(
      begin: const Offset(1, 0),
      end: Offset.zero,
    ).animate(CurvedAnimation(
      parent: animation,
      curve: Curves.easeInOut,
    )),
    child: child,
  );
}
