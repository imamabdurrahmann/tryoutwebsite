import 'dart:io';
import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:window_manager/window_manager.dart';
import 'core/theme/app_theme.dart';
import 'core/router/app_router.dart';
import 'data/sources/hive_source.dart';
import 'providers/user_provider.dart';

// Desktop check helper
bool get _isDesktop {
  if (kIsWeb) return false;
  return Platform.isWindows || Platform.isLinux || Platform.isMacOS;
}

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Optimize image cache for better performance when loading many images.
  final imageCache = PaintingBinding.instance.imageCache;
  imageCache.maximumSize = 200;
  imageCache.maximumSizeBytes = 100 << 20;

  // Init Hive — ringan, hanya setup database lokal
  await HiveSource.init();

  // Window Manager — Desktop only (skip di Web)
  if (_isDesktop) {
    await windowManager.ensureInitialized();

    final prefs = await SharedPreferences.getInstance();
    var savedWidth = prefs.getDouble('window_width') ?? 1024;
    var savedHeight = prefs.getDouble('window_height') ?? 720;
    if (savedWidth < 800 || savedHeight < 600) {
      savedWidth = 1024;
      savedHeight = 720;
      await prefs.setDouble('window_width', savedWidth);
      await prefs.setDouble('window_height', savedHeight);
    }

    final WindowOptions windowOptions = WindowOptions(
      size: Size(savedWidth, savedHeight),
      minimumSize: const Size(800, 600),
      center: true,
      title: 'JagoanCPNS',
      titleBarStyle: TitleBarStyle.normal,
    );

    windowManager.waitUntilReadyToShow(windowOptions, () async {
      await windowManager.show();
      await windowManager.focus();
    });
  }

  runApp(
    const ProviderScope(
      child: TryOutCPNSApp(),
    ),
  );
}

class TryOutCPNSApp extends ConsumerStatefulWidget {
  const TryOutCPNSApp({super.key});

  @override
  ConsumerState<TryOutCPNSApp> createState() => _TryOutCPNSAppState();
}

class _TryOutCPNSAppState extends ConsumerState<TryOutCPNSApp> with WindowListener {
  @override
  void initState() {
    super.initState();
    if (_isDesktop) {
      windowManager.addListener(this);
    }
  }

  @override
  void dispose() {
    if (_isDesktop) {
      windowManager.removeListener(this);
    }
    super.dispose();
  }

  /// Simpan ukuran window saat di-resize
  @override
  void onWindowResize() async {
    final size = await windowManager.getSize();
    final prefs = await SharedPreferences.getInstance();
    await prefs.setDouble('window_width', size.width);
    await prefs.setDouble('window_height', size.height);
  }

  @override
  Widget build(BuildContext context) {
    final isDarkMode = ref.watch(darkModeProvider);

    return MaterialApp.router(
      title: 'JagoanCPNS',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.lightTheme(),
      darkTheme: AppTheme.darkTheme(),
      themeMode: isDarkMode ? ThemeMode.dark : ThemeMode.light,
      routerConfig: appRouter,
    );
  }
}