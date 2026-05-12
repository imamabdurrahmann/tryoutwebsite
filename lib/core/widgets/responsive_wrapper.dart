import 'dart:io';
import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:flutter/material.dart';

/// Widget wrapper yang menyesuaikan layout berdasarkan platform.
/// Desktop (Windows/macOS/Linux): menggunakan maxWidth lebih lebar.
/// Mobile (Android/iOS): menggunakan full width.
class ResponsiveWrapper extends StatelessWidget {
  final Widget child;
  final double desktopMaxWidth;
  final double mobileMaxWidth;
  final EdgeInsetsGeometry? padding;

  const ResponsiveWrapper({
    super.key,
    required this.child,
    this.desktopMaxWidth = 900,
    this.mobileMaxWidth = 600,
    this.padding,
  });

  static bool get isDesktop {
    if (kIsWeb) return false;
    return Platform.isWindows || Platform.isLinux || Platform.isMacOS;
  }

  @override
  Widget build(BuildContext context) {
    final maxWidth = isDesktop ? desktopMaxWidth : mobileMaxWidth;

    return Center(
      child: ConstrainedBox(
        constraints: BoxConstraints(maxWidth: maxWidth),
        child: padding != null
            ? Padding(padding: padding!, child: child)
            : child,
      ),
    );
  }
}
