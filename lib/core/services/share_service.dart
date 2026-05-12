import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:url_launcher/url_launcher.dart';

class ShareService {
  /// Shares the try out result via WhatsApp or shows copy dialog
  static Future<void> shareResult({
    required String score,
    required String totalScore,
    required String category,
    required bool passed,
    required BuildContext context,
  }) async {
    final text = _buildShareText(
      score: score,
      totalScore: totalScore,
      category: category,
      passed: passed,
    );

    // On web, try native share API first, otherwise copy to clipboard
    if (kIsWeb) {
      await _shareOnWeb(context, text);
      return;
    }

    // On mobile, try WhatsApp first
    final shared = await _shareToWhatsApp(text);
    if (!shared) {
      // Fallback: show copy dialog
      if (context.mounted) {
        await _showCopyDialog(context, text);
      }
    }
  }

  static String _buildShareText({
    required String score,
    required String totalScore,
    required String category,
    required bool passed,
  }) {
    final status = passed ? 'LULUS' : 'TIDAK LULUS';
    final emoji = passed ? 'SELAMAT!' : 'TERUS SEMANGAT!';

    return '''
📊 Hasil Try Out JagoanCPNS

🧠 Skor: $score / $totalScore
✅ Status: $emoji $status

Latihan SKDCPNS di JagoanCPNS!
🔗 https://jagoancpns.vercel.app

#$category #JagoanCPNS #CPNS2025 #SKD
''';
  }

  static Future<bool> _shareToWhatsApp(String text) async {
    try {
      final encodedText = Uri.encodeComponent(text);
      final whatsappUrl = 'https://wa.me/?text=$encodedText';

      final uri = Uri.parse(whatsappUrl);
      if (await canLaunchUrl(uri)) {
        await launchUrl(uri, mode: LaunchMode.externalApplication);
        return true;
      }
    } catch (e) {
      debugPrint('Share to WhatsApp failed: $e');
    }
    return false;
  }

  static Future<void> _shareOnWeb(BuildContext context, String text) async {
    // Try Web Share API if available
    try {
      // Check if navigator.share is available
      // For now, show copy dialog as fallback
      await _showCopyDialog(context, text);
    } catch (e) {
      debugPrint('Web share failed: $e');
      if (context.mounted) {
        await _showCopyDialog(context, text);
      }
    }
  }

  static Future<void> _showCopyDialog(BuildContext context, String text) async {
    await Clipboard.setData(ClipboardData(text: text));

    if (context.mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: const Row(
            children: [
              Icon(Icons.check_circle, color: Colors.white, size: 20),
              SizedBox(width: 12),
              Expanded(
                child: Text('Hasil telah disalin ke clipboard!'),
              ),
            ],
          ),
          backgroundColor: Colors.green.shade700,
          behavior: SnackBarBehavior.floating,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
          margin: const EdgeInsets.all(16),
          duration: const Duration(seconds: 3),
        ),
      );
    }
  }

  /// Shows a share bottom sheet with multiple options
  static Future<void> showShareSheet({
    required BuildContext context,
    required String score,
    required String totalScore,
    required String category,
    required bool passed,
  }) async {
    final text = _buildShareText(
      score: score,
      totalScore: totalScore,
      category: category,
      passed: passed,
    );

    await showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      builder: (context) => Container(
        padding: const EdgeInsets.all(20),
        decoration: BoxDecoration(
          color: Theme.of(context).scaffoldBackgroundColor,
          borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
        ),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Container(
              width: 40,
              height: 4,
              decoration: BoxDecoration(
                color: Colors.grey.shade300,
                borderRadius: BorderRadius.circular(2),
              ),
            ),
            const SizedBox(height: 20),
            const Text(
              'Bagikan Hasil',
              style: TextStyle(
                fontSize: 20,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 8),
            Text(
              'Pilih platform untuk membagikan hasil try out kamu',
              style: TextStyle(
                color: Colors.grey.shade600,
                fontSize: 14,
              ),
            ),
            const SizedBox(height: 24),
            // WhatsApp option
            _ShareOption(
              icon: Icons.chat_bubble,
              iconColor: const Color(0xFF25D366),
              label: 'WhatsApp',
              onTap: () async {
                Navigator.pop(context);
                await _shareToWhatsApp(text);
              },
            ),
            const SizedBox(height: 12),
            // Copy to clipboard option
            _ShareOption(
              icon: Icons.copy,
              iconColor: Colors.blue,
              label: 'Salin ke Clipboard',
              onTap: () async {
                Navigator.pop(context);
                await Clipboard.setData(ClipboardData(text: text));
                if (context.mounted) {
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(
                      content: const Text('Hasil telah disalin ke clipboard!'),
                      backgroundColor: Colors.green.shade700,
                      behavior: SnackBarBehavior.floating,
                      shape: const RoundedRectangleBorder(
                        borderRadius: BorderRadius.all(Radius.circular(10)),
                      ),
                      margin: const EdgeInsets.all(16),
                    ),
                  );
                }
              },
            ),
            const SizedBox(height: 24),
          ],
        ),
      ),
    );
  }
}

class _ShareOption extends StatelessWidget {
  final IconData icon;
  final Color iconColor;
  final String label;
  final VoidCallback onTap;

  const _ShareOption({
    required this.icon,
    required this.iconColor,
    required this.label,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.transparent,
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(12),
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
          decoration: BoxDecoration(
            border: Border.all(color: Colors.grey.shade200),
            borderRadius: BorderRadius.circular(12),
          ),
          child: Row(
            children: [
              Container(
                padding: const EdgeInsets.all(10),
                decoration: BoxDecoration(
                  color: iconColor.withAlpha(25),
                  shape: BoxShape.circle,
                ),
                child: Icon(icon, color: iconColor, size: 24),
              ),
              const SizedBox(width: 16),
              Expanded(
                child: Text(
                  label,
                  style: const TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.w500,
                  ),
                ),
              ),
              Icon(
                Icons.chevron_right,
                color: Colors.grey.shade400,
              ),
            ],
          ),
        ),
      ),
    );
  }
}