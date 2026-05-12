import 'package:flutter/material.dart';

/// Shared utility class to avoid code duplication across widgets.
class AppUtils {
  AppUtils._();

  /// Parse color from shape code string.
  /// Used by question_card, review_question_card, and figural_question_widget.
  static Color parseColor(String code, Color defaultColor) {
    final lower = code.toLowerCase();
    if (lower.contains('red')) return Colors.red;
    if (lower.contains('blue')) return Colors.blue;
    if (lower.contains('green')) return Colors.green;
    if (lower.contains('orange')) return Colors.orange;
    if (lower.contains('purple')) return Colors.purple;
    if (lower.contains('cyan')) return Colors.cyan;
    if (lower.contains('pink')) return Colors.pink;
    if (lower.contains('brown')) return Colors.brown;
    if (lower.contains('yellow')) return Colors.amber;
    if (lower.contains('black')) return Colors.black87;
    if (lower.contains('white')) return Colors.white;
    return defaultColor;
  }

  /// Format duration in seconds to mm:ss string.
  static String formatDuration(int seconds) {
    final m = seconds ~/ 60;
    final s = seconds % 60;
    return '${m.toString().padLeft(2, '0')}:${s.toString().padLeft(2, '0')}';
  }

  /// Credit banner widget used on Home and Profile screens.
  static Widget buildCreditBanner(BuildContext context) {
    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 16),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.primary.withAlpha(10),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: Theme.of(context).colorScheme.primary.withAlpha(30),
          width: 1,
        ),
      ),
      child: Center(
        child: RichText(
          textAlign: TextAlign.center,
          text: TextSpan(
            style: Theme.of(context).textTheme.bodySmall?.copyWith(
                  color: Colors.grey.shade700,
                ),
            children: [
              const TextSpan(text: 'TryOutCPNSbyIMAM 100% Gratis\n'),
              TextSpan(
                text: 'Crafted by ',
                style: Theme.of(context).textTheme.bodySmall?.copyWith(
                      color: Colors.grey.shade700,
                    ),
              ),
              TextSpan(
                text: 'Abdurrahman',
                style: TextStyle(
                  color: Theme.of(context).colorScheme.primary,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const TextSpan(text: ' 🚀'),
            ],
          ),
        ),
      ),
    );
  }
}
