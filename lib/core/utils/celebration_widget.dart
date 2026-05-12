import 'dart:math';
import 'package:flutter/material.dart';

/// A lightweight confetti/celebration widget that shows falling particles.
/// No external packages needed.
class CelebrationWidget extends StatefulWidget {
  final bool show;
  final Duration duration;

  const CelebrationWidget({
    super.key,
    this.show = true,
    this.duration = const Duration(seconds: 4),
  });

  @override
  State<CelebrationWidget> createState() => _CelebrationWidgetState();
}

class _CelebrationWidgetState extends State<CelebrationWidget>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  final List<_ConfettiParticle> _particles = [];
  final Random _random = Random();

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: widget.duration,
    );

    if (widget.show) {
      _generateParticles();
      _controller.forward();
    }
  }

  void _generateParticles() {
    _particles.clear();
    for (int i = 0; i < 60; i++) {
      _particles.add(_ConfettiParticle(
        x: _random.nextDouble(),
        speed: 0.3 + _random.nextDouble() * 0.7,
        size: 4 + _random.nextDouble() * 8,
        color: _confettiColors[_random.nextInt(_confettiColors.length)],
        angle: _random.nextDouble() * 2 * pi,
        rotationSpeed: (_random.nextDouble() - 0.5) * 10,
        swayAmplitude: 0.02 + _random.nextDouble() * 0.04,
        swayFrequency: 1 + _random.nextDouble() * 3,
        delay: _random.nextDouble() * 0.3,
      ));
    }
  }

  static const List<Color> _confettiColors = [
    Color(0xFFE53935), // Red
    Color(0xFF1E88E5), // Blue
    Color(0xFF43A047), // Green
    Color(0xFFFDD835), // Yellow
    Color(0xFFE91E63), // Pink
    Color(0xFF8E24AA), // Purple
    Color(0xFFFF6F00), // Orange
    Color(0xFF00ACC1), // Cyan
  ];

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    if (!widget.show) return const SizedBox.shrink();

    return AnimatedBuilder(
      animation: _controller,
      builder: (context, child) {
        return CustomPaint(
          size: Size.infinite,
          painter: _ConfettiPainter(
            particles: _particles,
            progress: _controller.value,
          ),
        );
      },
    );
  }
}

class _ConfettiParticle {
  final double x;
  final double speed;
  final double size;
  final Color color;
  final double angle;
  final double rotationSpeed;
  final double swayAmplitude;
  final double swayFrequency;
  final double delay;

  _ConfettiParticle({
    required this.x,
    required this.speed,
    required this.size,
    required this.color,
    required this.angle,
    required this.rotationSpeed,
    required this.swayAmplitude,
    required this.swayFrequency,
    required this.delay,
  });
}

class _ConfettiPainter extends CustomPainter {
  final List<_ConfettiParticle> particles;
  final double progress;

  _ConfettiPainter({required this.particles, required this.progress});

  @override
  void paint(Canvas canvas, Size size) {
    for (final p in particles) {
      final adjustedProgress = ((progress - p.delay) / (1 - p.delay)).clamp(0.0, 1.0);
      if (adjustedProgress <= 0) continue;

      final opacity = adjustedProgress < 0.8 ? 1.0 : (1.0 - adjustedProgress) / 0.2;
      final paint = Paint()
        ..color = p.color.withAlpha((opacity * 255).round())
        ..style = PaintingStyle.fill;

      final y = adjustedProgress * size.height * p.speed * 1.5;
      final sway = sin(adjustedProgress * p.swayFrequency * 2 * pi) * p.swayAmplitude * size.width;
      final x = p.x * size.width + sway;
      final rotation = p.angle + adjustedProgress * p.rotationSpeed;

      canvas.save();
      canvas.translate(x, y);
      canvas.rotate(rotation);

      // Draw rectangle confetti
      final rect = Rect.fromCenter(
        center: Offset.zero,
        width: p.size,
        height: p.size * 0.6,
      );
      canvas.drawRect(rect, paint);
      canvas.restore();
    }
  }

  @override
  bool shouldRepaint(covariant _ConfettiPainter oldDelegate) =>
      oldDelegate.progress != progress;
}
