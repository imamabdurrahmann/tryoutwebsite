import 'package:flutter/material.dart';

/// A wrapper widget that constrains content width for desktop screens.
/// On mobile-sized screens, it takes full width.
/// On desktop, it centers the content with a max width.
class ResponsiveWrapper extends StatelessWidget {
  final Widget child;
  final double maxWidth;
  final EdgeInsets? padding;

  const ResponsiveWrapper({
    super.key,
    required this.child,
    this.maxWidth = 800,
    this.padding,
  });

  @override
  Widget build(BuildContext context) {
    return Center(
      child: ConstrainedBox(
        constraints: BoxConstraints(maxWidth: maxWidth),
        child: padding != null
            ? Padding(padding: padding!, child: child)
            : child,
      ),
    );
  }

  /// Check if we are on a wide (desktop) screen
  static bool isDesktop(BuildContext context) {
    return MediaQuery.of(context).size.width > 900;
  }

  /// Check if we are on a tablet-sized screen
  static bool isTablet(BuildContext context) {
    final w = MediaQuery.of(context).size.width;
    return w > 600 && w <= 900;
  }
}
