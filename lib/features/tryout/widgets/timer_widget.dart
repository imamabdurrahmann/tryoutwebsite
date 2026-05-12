import 'package:flutter/material.dart';
import '../../../core/theme/app_theme.dart';

class TimerWidget extends StatefulWidget {
  final int remainingSeconds;
  final VoidCallback? onTimeUp;

  const TimerWidget({
    super.key,
    required this.remainingSeconds,
    this.onTimeUp,
  });

  @override
  State<TimerWidget> createState() => _TimerWidgetState();
}

class _TimerWidgetState extends State<TimerWidget>
    with SingleTickerProviderStateMixin {
  late AnimationController _blinkController;
  late Animation<double> _blinkAnimation;

  @override
  void initState() {
    super.initState();
    _blinkController = AnimationController(
      duration: const Duration(milliseconds: 600),
      vsync: this,
    );
    _blinkAnimation = Tween<double>(begin: 1.0, end: 0.3).animate(
      CurvedAnimation(parent: _blinkController, curve: Curves.easeInOut),
    );
  }

  @override
  void didUpdateWidget(covariant TimerWidget oldWidget) {
    super.didUpdateWidget(oldWidget);
    // Start blinking when time drops to < 5 menit
    final isLowTime = widget.remainingSeconds < 300 && widget.remainingSeconds > 0;
    final wasLowTime = oldWidget.remainingSeconds < 300;

    if (isLowTime && !wasLowTime) {
      _blinkController.repeat(reverse: true);
    } else if (!isLowTime && wasLowTime) {
      _blinkController.stop();
      _blinkController.reset();
    }

    // Trigger callback when time reaches 0
    if (widget.remainingSeconds == 0 && oldWidget.remainingSeconds > 0) {
      widget.onTimeUp?.call();
    }
  }

  @override
  void dispose() {
    _blinkController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final totalMinutes = widget.remainingSeconds ~/ 60;
    final totalSeconds = widget.remainingSeconds % 60;

    // Tampilkan jam:jika lebih dari 60 menit
    final isOverHour = totalMinutes >= 60;
    final displayMinutes = isOverHour ? totalMinutes : totalMinutes;
    final displayHours = totalMinutes ~/ 60;

    final isLowTime = widget.remainingSeconds < 300; // < 5 menit
    final isCritical = widget.remainingSeconds < 60; // < 1 menit
    final isTimeUp = widget.remainingSeconds <= 0;

    String timeString;
    if (isOverHour) {
      final h = displayHours;
      final m = displayMinutes % 60;
      timeString = '${h.toString().padLeft(2, '0')}:${m.toString().padLeft(2, '0')}:${totalSeconds.toString().padLeft(2, '0')}';
    } else {
      timeString = '${displayMinutes.toString().padLeft(2, '0')}:${totalSeconds.toString().padLeft(2, '0')}';
    }

    // Warna berdasarkan kondisi waktu
    Color timeColor;
    Color bgColor;
    Color iconColor;

    if (isTimeUp) {
      timeColor = Colors.white;
      bgColor = Colors.grey.shade700;
      iconColor = Colors.white70;
    } else if (isCritical) {
      timeColor = Colors.white;
      bgColor = AppTheme.errorRed;
      iconColor = Colors.white;
    } else if (isLowTime) {
      timeColor = Colors.white;
      bgColor = AppTheme.warningOrange;
      iconColor = Colors.white;
    } else {
      timeColor = Colors.white;
      bgColor = Colors.white.withAlpha(25);
      iconColor = Colors.white70;
    }

    final timerContent = Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
      decoration: BoxDecoration(
        color: bgColor,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(
          color: isLowTime ? Colors.white30 : Colors.white10,
          width: 1,
        ),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(
            isTimeUp
                ? Icons.alarm_off
                : (isCritical ? Icons.warning : Icons.timer),
            size: 18,
            color: iconColor,
          ),
          const SizedBox(width: 6),
          Text(
            timeString,
            style: TextStyle(
              color: timeColor,
              fontWeight: FontWeight.bold,
              fontSize: 15,
              fontFamily: 'monospace',
              letterSpacing: 1,
            ),
          ),
          if (isLowTime && !isTimeUp) ...[
            const SizedBox(width: 6),
            Icon(
              Icons.priority_high,
              size: 14,
              color: Colors.white.withAlpha(180),
            ),
          ],
        ],
      ),
    );

    // Bungkus dengan blinking animation jika waktu rendah
    if (isLowTime && !isTimeUp) {
      return AnimatedBuilder(
        animation: _blinkAnimation,
        builder: (context, child) {
          return Opacity(
            opacity: _blinkAnimation.value,
            child: timerContent,
          );
        },
      );
    }

    return timerContent;
  }
}
