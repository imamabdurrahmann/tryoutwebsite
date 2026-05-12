import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart' show kIsWeb;

/// Paket kartu elegan dengan desain glassmorphism.
/// Bersifat reusable untuk semua menu utama di aplikasi.
class PackageCard extends StatelessWidget {
  final String title;
  final String subtitle;
  final IconData icon;
  final Color color;
  final VoidCallback onTap;
  final bool largeIcon;

  const PackageCard({
    super.key,
    required this.title,
    required this.subtitle,
    required this.icon,
    required this.color,
    required this.onTap,
    this.largeIcon = false,
  });

  @override
  Widget build(BuildContext context) {
    final isDark = Theme.of(context).brightness == Brightness.dark;
    final isWeb = kIsWeb;

    return Card(
      elevation: 0,
      clipBehavior: Clip.antiAlias,
      shadowColor: color.withAlpha(60),
      child: InkWell(
        onTap: onTap,
        splashColor: color.withAlpha(25),
        highlightColor: color.withAlpha(12),
        child: Container(
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(isWeb ? 12 : 16),
            gradient: LinearGradient(
              colors: isDark
                  ? [
                      color.withAlpha(40),
                      color.withAlpha(20),
                    ]
                  : [
                      color.withAlpha(30),
                      color.withAlpha(10),
                    ],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
            border: Border.all(
              color: color.withAlpha(isDark ? 50 : 40),
              width: 1,
            ),
          ),
          child: Stack(
            children: [
              // Corner decoration
              Positioned(
                right: -10,
                top: -10,
                child: Container(
                  width: 60,
                  height: 60,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: color.withAlpha(isDark ? 20 : 15),
                  ),
                ),
              ),
              // Content
              Padding(
                padding: const EdgeInsets.all(14),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    // Icon dalam lingkaran
                    Container(
                      padding: EdgeInsets.all(largeIcon ? 12 : 10),
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
                      child: Icon(
                        icon,
                        color: color,
                        size: largeIcon ? 26 : 22,
                      ),
                    ),
                    const SizedBox(height: 10),
                    // Judul
                    Flexible(
                      child: Text(
                        title,
                        maxLines: 2,
                        overflow: TextOverflow.ellipsis,
                        style: Theme.of(context).textTheme.titleMedium?.copyWith(
                              fontWeight: FontWeight.w800,
                              color: color,
                              height: 1.2,
                            ),
                      ),
                    ),
                    if (subtitle.isNotEmpty) ...[
                      const SizedBox(height: 4),
                      // Subtitle
                      Text(
                        subtitle,
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: Theme.of(context).textTheme.bodySmall?.copyWith(
                              color: Colors.grey.shade600,
                              fontWeight: FontWeight.w500,
                            ),
                      ),
                    ],
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
