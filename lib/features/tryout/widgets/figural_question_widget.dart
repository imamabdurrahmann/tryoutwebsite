import 'dart:math';
import 'dart:convert';
import 'package:flutter/material.dart';
import '../../../core/utils/app_utils.dart';

enum FiguralType {
  /// Deret bentuk berulang (mis: kotak, lingkaran, segitiga, ?, ?, ?)
  deret,

  /// Rotasi bentuk (panah diputar 90° per langkah)
  rotasi,

  /// Matriks 3x3 dengan pola tertentu, satu sel kosong
  matriks,

  /// Bayangan/cermin bentuk
  bayangan,
}

/// Semua kode bentuk yang didukung oleh ShapePainter
enum ShapeCode {
  circle,
  square,
  triangle,
  diamond,
  arrowUp,
  arrowDown,
  arrowLeft,
  arrowRight,
  pentagon,
  hexagon,
  star,
  cross,
  plus,
  stickmanV1,
  stickmanV2,
  stickmanV3,
  stickmanA1,
  stickmanA2,
  stickmanA3,
}

/// Data lengkap untuk soal figural.
/// Disimpan sebagai JSON string di Question.figuralData.
class FiguralData {
  final FiguralType type;
  final List<String> sequence;
  final String? pattern;
  final List<List<String>>? gridData;
  final List<String> answerShapes; // Changed to List<String>
  final int correctIndex;

  const FiguralData({
    required this.type,
    required this.sequence,
    this.pattern,
    this.gridData,
    this.answerShapes = const [],
    this.correctIndex = 0,
  });

  factory FiguralData.fromJson(Map<String, dynamic> json) {
    // Parse answerShapes safely, could be string "A,B,C" or List ["A", "B"]
    List<String> parsedAnswerShapes = [];
    if (json['answerShapes'] is List) {
      parsedAnswerShapes = List<String>.from(json['answerShapes']);
    } else if (json['answerShapes'] is String) {
      parsedAnswerShapes = (json['answerShapes'] as String).split(',');
    }

    return FiguralData(
      type: FiguralType.values.firstWhere(
        (e) => e.name == json['type'],
        orElse: () => FiguralType.deret,
      ),
      sequence: List<String>.from(json['sequence'] ?? []),
      pattern: json['pattern'],
      gridData: json['gridData'] != null
          ? (json['gridData'] as List)
              .map((row) => List<String>.from(row))
              .toList()
          : null,
      answerShapes: parsedAnswerShapes,
      correctIndex: json['correctIndex'] ?? 0,
    );
  }

  Map<String, dynamic> toJson() => {
        'type': type.name,
        'sequence': sequence,
        if (pattern != null) 'pattern': pattern,
        if (gridData != null) 'gridData': gridData,
        if (answerShapes.isNotEmpty) 'answerShapes': answerShapes,
        'correctIndex': correctIndex,
      };

  List<String> get answerShapeList => answerShapes;
}

// ============================================================================
// SHAPE PAINTER — CustomPainter yang menggambar bentuk
// ============================================================================

class ShapePainter extends CustomPainter {
  final ShapeCode code;
  final Color color;
  final double size;
  final bool filled;
  final double rotation; // dalam derajat

  ShapePainter({
    required this.code,
    this.color = Colors.black,
    this.size = 40,
    this.filled = true,
    this.rotation = 0,
  });

  @override
  void paint(Canvas canvas, Size size2) {
    final paint = Paint()
      ..color = color
      ..style = filled ? PaintingStyle.fill : PaintingStyle.stroke
      ..strokeWidth = 2;

    final paintOutline = Paint()
      ..color = color
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2.5;

    final center = Offset(size2.width / 2, size2.height / 2);
    final half = min(size2.width, size2.height) / 2 * 0.85;

    canvas.save();
    canvas.translate(center.dx, center.dy);
    canvas.rotate(rotation * pi / 180);
    canvas.translate(-center.dx, -center.dy);

    switch (code) {
      case ShapeCode.circle:
        canvas.drawCircle(center, half, filled ? paint : paintOutline);

      case ShapeCode.square:
        final rect = Rect.fromCenter(
          center: center,
          width: half * 1.7,
          height: half * 1.7,
        );
        canvas.drawRect(rect, filled ? paint : paintOutline);

      case ShapeCode.triangle:
        _drawPolygon(canvas, center, half, 3, filled ? paint : paintOutline);

      case ShapeCode.diamond:
        _drawPolygon(canvas, center, half, 4, filled ? paint : paintOutline);

      case ShapeCode.arrowUp:
        _drawArrow(canvas, center, half, 0, filled ? paint : paintOutline);

      case ShapeCode.arrowDown:
        _drawArrow(canvas, center, half, 180, filled ? paint : paintOutline);

      case ShapeCode.arrowLeft:
        _drawArrow(canvas, center, half, 270, filled ? paint : paintOutline);

      case ShapeCode.arrowRight:
        _drawArrow(canvas, center, half, 90, filled ? paint : paintOutline);

      case ShapeCode.pentagon:
        _drawPolygon(canvas, center, half, 5, filled ? paint : paintOutline);

      case ShapeCode.hexagon:
        _drawPolygon(canvas, center, half, 6, filled ? paint : paintOutline);

      case ShapeCode.star:
        _drawStar(canvas, center, half, filled ? paint : paintOutline);

      case ShapeCode.cross:
        _drawCross(canvas, center, half, filled ? paint : paintOutline);

      case ShapeCode.plus:
        _drawCross(canvas, center, half, filled ? paint : paintOutline, plus: true);

      case ShapeCode.stickmanV1:
        _drawStickman(canvas, center, half, filled ? paint : paintOutline, 1, false);
      case ShapeCode.stickmanV2:
        _drawStickman(canvas, center, half, filled ? paint : paintOutline, 2, false);
      case ShapeCode.stickmanV3:
        _drawStickman(canvas, center, half, filled ? paint : paintOutline, 3, false);
      case ShapeCode.stickmanA1:
        _drawStickman(canvas, center, half, filled ? paint : paintOutline, 1, true);
      case ShapeCode.stickmanA2:
        _drawStickman(canvas, center, half, filled ? paint : paintOutline, 2, true);
      case ShapeCode.stickmanA3:
        _drawStickman(canvas, center, half, filled ? paint : paintOutline, 3, true);
    }

    canvas.restore();
  }

  void _drawPolygon(Canvas canvas, Offset center, double radius, int sides,
      Paint paint) {
    final path = Path();
    for (int i = 0; i < sides; i++) {
      final angle = (2 * pi / sides) * i - pi / 2;
      final x = center.dx + radius * cos(angle);
      final y = center.dy + radius * sin(angle);
      if (i == 0) {
        path.moveTo(x, y);
      } else {
        path.lineTo(x, y);
      }
    }
    path.close();
    canvas.drawPath(path, paint);
  }

  void _drawArrow(Canvas canvas, Offset center, double radius, double baseAngle,
      Paint paint) {
    final arrowAngle = (baseAngle) * pi / 180;
    final tipX = center.dx + radius * cos(arrowAngle - pi / 2);
    final tipY = center.dy + radius * sin(arrowAngle - pi / 2);

    final leftAngle = arrowAngle + pi * 0.8;
    final rightAngle = arrowAngle - pi * 0.8;
    final leftX = center.dx + radius * 0.6 * cos(leftAngle - pi / 2);
    final leftY = center.dy + radius * 0.6 * sin(leftAngle - pi / 2);
    final rightX = center.dx + radius * 0.6 * cos(rightAngle - pi / 2);
    final rightY = center.dy + radius * 0.6 * sin(rightAngle - pi / 2);

    final backX = center.dx - radius * 0.5 * cos(arrowAngle - pi / 2);
    final backY = center.dy - radius * 0.5 * sin(arrowAngle - pi / 2);

    final path = Path()
      ..moveTo(tipX, tipY)
      ..lineTo(leftX, leftY)
      ..lineTo(backX, backY)
      ..lineTo(rightX, rightY)
      ..close();

    canvas.drawPath(path, paint);
  }

  void _drawStar(Canvas canvas, Offset center, double radius, Paint paint) {
    final path = Path();
    for (int i = 0; i < 10; i++) {
      final r = i.isEven ? radius : radius * 0.4;
      final angle = (2 * pi / 10) * i - pi / 2;
      final x = center.dx + r * cos(angle);
      final y = center.dy + r * sin(angle);
      if (i == 0) {
        path.moveTo(x, y);
      } else {
        path.lineTo(x, y);
      }
    }
    path.close();
    canvas.drawPath(path, paint);
  }

  void _drawCross(Canvas canvas, Offset center, double radius, Paint paint,
      {bool plus = false}) {
    final w = radius * 0.35;
    final l = radius * 1.4;

    final path = Path()
      ..addRect(Rect.fromCenter(center: center, width: l, height: w))
      ..addRect(Rect.fromCenter(center: center, width: w, height: l));
    if (plus) {
      canvas.drawPath(path, paint);
    } else {
      final path2 = Path()
        ..moveTo(center.dx - l / 2, center.dy - l / 2)
        ..lineTo(center.dx + l / 2, center.dy + l / 2);
      final path3 = Path()
        ..moveTo(center.dx + l / 2, center.dy - l / 2)
        ..lineTo(center.dx - l / 2, center.dy + l / 2);
      canvas.drawPath(path, paint);
      canvas.drawPath(path2, paint);
      canvas.drawPath(path3, paint);
    }
  }

  void _drawStickman(Canvas canvas, Offset center, double radius, Paint paint, int count, bool isA) {
    final spacing = radius * 0.65;
    List<Offset> centers = [];
    if (count == 1) {
      centers.add(center);
    } else if (count == 2) {
      centers.add(Offset(center.dx - spacing / 1.1, center.dy));
      centers.add(Offset(center.dx + spacing / 1.1, center.dy));
    } else if (count == 3) {
      centers.add(Offset(center.dx - spacing * 1.3, center.dy));
      centers.add(center);
      centers.add(Offset(center.dx + spacing * 1.3, center.dy));
    }

    final p = Paint()
      ..color = paint.color
      ..style = PaintingStyle.fill
      ..strokeWidth = paint.strokeWidth;
      
    final lineP = Paint()
      ..color = paint.color
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2.5;

    for (var c in centers) {
      // Head
      final headRadius = radius * 0.22;
      final headCenter = Offset(c.dx, c.dy - radius * 0.5);
      canvas.drawCircle(headCenter, headRadius, p);

      // Body
      final neckY = headCenter.dy + headRadius;
      final bottomY = c.dy + radius * 0.3;
      canvas.drawLine(Offset(c.dx, neckY), Offset(c.dx, bottomY), lineP);

      // Legs
      final footY = c.dy + radius * 0.9;
      final legSpread = radius * 0.25;
      final leftFoot = Offset(c.dx - legSpread, footY);
      final rightFoot = Offset(c.dx + legSpread, footY);
      
      canvas.drawLine(Offset(c.dx, bottomY), leftFoot, lineP);
      canvas.drawLine(Offset(c.dx, bottomY), rightFoot, lineP);

      if (isA) {
        // Horizontal line across legs (A shape)
        final midLegY = c.dy + radius * 0.6;
        final midSpread = legSpread * 0.5; // halfway down the leg
        canvas.drawLine(Offset(c.dx - midSpread, midLegY), Offset(c.dx + midSpread, midLegY), lineP);
      }
    }
  }

  @override
  bool shouldRepaint(covariant ShapePainter oldDelegate) =>
      oldDelegate.code != code ||
      oldDelegate.color != color ||
      oldDelegate.size != size ||
      oldDelegate.filled != filled ||
      oldDelegate.rotation != rotation;
}

/// CustomPainter: draws a dashed rectangle border (for ? placeholder cell)
class _DashedBorderPainter extends CustomPainter {
  final Color color;
  final double strokeWidth;
  final double borderRadius;
  final double dashWidth;
  final double dashSpace;

  const _DashedBorderPainter({
    required this.color,
    this.strokeWidth = 2,
    this.borderRadius = 8,
    double dashWidth = 6,
    double dashSpace = 4,
  })  : dashWidth = dashWidth,
        dashSpace = dashSpace;

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = color
      ..strokeWidth = strokeWidth
      ..style = PaintingStyle.stroke;

    final rrect = RRect.fromRectAndRadius(
      Rect.fromLTWH(strokeWidth / 2, strokeWidth / 2,
          size.width - strokeWidth, size.height - strokeWidth),
      Radius.circular(borderRadius),
    );

    final path = Path()..addRRect(rrect);
    final dashPath = Path();

    for (final metric in path.computeMetrics()) {
      double distance = 0;
      while (distance < metric.length) {
        dashPath.addPath(
          metric.extractPath(distance, distance + dashWidth),
          Offset.zero,
        );
        distance += dashWidth + dashSpace;
      }
    }

    canvas.drawPath(dashPath, paint);
  }

  @override
  bool shouldRepaint(covariant _DashedBorderPainter oldDelegate) =>
      oldDelegate.color != color ||
      oldDelegate.strokeWidth != strokeWidth ||
      oldDelegate.borderRadius != borderRadius ||
      oldDelegate.dashWidth != dashWidth ||
      oldDelegate.dashSpace != dashSpace;
}

// ============================================================================
// SHAPE WIDGET — Wrapper widget untuk ShapeCode
// ============================================================================

class ShapeWidget extends StatelessWidget {
  final String code;
  final Color color;
  final double size;
  final bool filled;
  final double rotation;

  const ShapeWidget({
    super.key,
    required this.code,
    this.color = Colors.black87,
    this.size = 44,
    this.filled = true,
    this.rotation = 0,
  });

  ShapeCode? _parseCode(String c) {
    final lower = c.toLowerCase().replaceAll('-', '_');
    if (lower.contains('circle')) return ShapeCode.circle;
    if (lower.contains('square') || lower.contains('box')) return ShapeCode.square;
    if (lower.contains('triangle')) return ShapeCode.triangle;
    if (lower.contains('diamond')) return ShapeCode.diamond;
    if (lower.contains('arrow_up')) return ShapeCode.arrowUp;
    if (lower.contains('arrow_down')) return ShapeCode.arrowDown;
    if (lower.contains('arrow_left')) return ShapeCode.arrowLeft;
    if (lower.contains('arrow_right')) return ShapeCode.arrowRight;
    if (lower.contains('pentagon')) return ShapeCode.pentagon;
    if (lower.contains('hexagon')) return ShapeCode.hexagon;
    if (lower.contains('star')) return ShapeCode.star;
    if (lower.contains('cross')) return ShapeCode.cross;
    if (lower.contains('plus')) return ShapeCode.plus;

    if (lower.contains('stickman')) {
      bool isA = lower.contains('a_') || lower.contains('_a') || lower.contains('a-') || lower.contains('-a') || lower.contains('a');
      // Perbaikan: isA mungkin tidak sengaja true kalau 'a' muncul, jadi kita cek spesifik:
      isA = lower.contains('-a') || lower.contains('_a') || lower.contains('a-');
      int count = 1;
      if (lower.contains('2')) count = 2;
      if (lower.contains('3')) count = 3;
      
      if (isA) {
        if (count == 1) return ShapeCode.stickmanA1;
        if (count == 2) return ShapeCode.stickmanA2;
        if (count == 3) return ShapeCode.stickmanA3;
      } else {
        if (count == 1) return ShapeCode.stickmanV1;
        if (count == 2) return ShapeCode.stickmanV2;
        if (count == 3) return ShapeCode.stickmanV3;
      }
    }

    if (lower == 'empty' || lower == 'blank') return null;
    return null;
  }



  Widget _buildPlaceholder() {
    return Container(
      width: size,
      height: size,
      decoration: BoxDecoration(
        color: Colors.amber.shade50,
        borderRadius: BorderRadius.circular(8),
      ),
      child: CustomPaint(
        painter: _DashedBorderPainter(
          color: Colors.amber.shade700,
          strokeWidth: 2.5,
          borderRadius: 8,
        ),
        child: Center(
          child: Text(
            '?',
            style: TextStyle(
              fontSize: size * 0.45,
              fontWeight: FontWeight.bold,
              color: Colors.amber.shade800,
            ),
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    // 1. Cek apakah ini adalah file aset gambar (PNG/JPG)
    if (code.toLowerCase().endsWith('.png') || 
        code.toLowerCase().endsWith('.jpg') || 
        code.toLowerCase().endsWith('.jpeg')) {
      return Transform.rotate(
        angle: rotation * pi / 180,
        child: Image.asset(
          code,
          width: size,
          height: size,
          fit: BoxFit.contain,
          errorBuilder: (context, error, stackTrace) {
            return const Icon(Icons.broken_image, color: Colors.grey);
          },
        ),
      );
    }

    // 2. Jika bukan gambar, parsing menggunakan kode bentuk manual (lingkaran, kotak, stickman, dll)
    final shapeCode = _parseCode(code);
    final shapeColor = AppUtils.parseColor(code, color);

    // Kotak kosong untuk jawaban (tanda ? = pola yang tidak dikenali/harus diisi)
    if (shapeCode == null) {
      return _buildPlaceholder();
    }

    return CustomPaint(
      size: Size(size, size),
      painter: ShapePainter(
        code: shapeCode,
        color: shapeColor,
        size: size,
        filled: filled,
        rotation: rotation,
      ),
    );
  }
}

// ============================================================================
// DERET FIGURAL WIDGET
// ============================================================================

class DeretFiguralWidget extends StatelessWidget {
  final List<String> shapes;
  final Color color;
  final double shapeSize;
  final int? answerIndex;
  final List<String>? choices;

  const DeretFiguralWidget({
    super.key,
    required this.shapes,
    this.color = Colors.black87,
    this.shapeSize = 48,
    this.answerIndex,
    this.choices,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        // Deret utama dalam Wrap agar jika layar kecil, gambar turun ke baris bawahnya (tidak terpotong)
        Wrap(
          alignment: WrapAlignment.center,
          crossAxisAlignment: WrapCrossAlignment.center,
          spacing: 4.0,
          runSpacing: 12.0,
          children: [
              for (int i = 0; i < shapes.length; i++) ...[
                // Kotak bentuk (NO border kuning, hanya border standar)
                Container(
                  padding: const EdgeInsets.all(6),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    border: Border.all(color: Colors.grey.shade400, width: 1.5),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: ShapeWidget(
                    code: shapes[i],
                    color: color,
                    size: shapeSize,
                  ),
                ),
                // Tanda panah pemisah antar gambar (KECUALI setelah gambar terakhir SEBELUM ?)
                if (i < shapes.length - 1)
                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 8),
                    child: Icon(
                      Icons.arrow_forward,
                      color: Colors.grey.shade600,
                      size: 24,
                    ),
                  ),
              ],
              // Tanda panah sebelum kotak ?
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 8),
                child: Icon(
                  Icons.arrow_forward,
                  color: Colors.grey.shade600,
                  size: 24,
                ),
              ),
              // KOTAK TANDA TANYA - jawaban yang harus dicari
              Container(
                width: shapeSize + 12,
                height: shapeSize + 12,
                padding: const EdgeInsets.all(6),
                decoration: BoxDecoration(
                  color: Colors.amber.shade50,
                  border: Border.all(color: Colors.amber.shade700, width: 2),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Center(
                  child: Text(
                    '?',
                    style: TextStyle(
                      fontSize: shapeSize * 0.45,
                      fontWeight: FontWeight.bold,
                      color: Colors.amber.shade800,
                    ),
                  ),
                ),
              ),
            ],
          ),
      ],
    );
  }
}

// ============================================================================
// ROTASI FIGURAL WIDGET
// ============================================================================

class RotasiFiguralWidget extends StatelessWidget {
  final List<String> shapes;
  final List<int>? rotations;
  final Color color;
  final double shapeSize;
  final List<String>? choices;

  const RotasiFiguralWidget({
    super.key,
    required this.shapes,
    this.rotations,
    this.color = Colors.black87,
    this.shapeSize = 48,
    this.choices,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Wrap(
          alignment: WrapAlignment.center,
          crossAxisAlignment: WrapCrossAlignment.center,
          spacing: 4.0,
          runSpacing: 12.0,
          children: [
              for (int i = 0; i < shapes.length; i++) ...[
                Container(
                  padding: const EdgeInsets.all(6),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    border: Border.all(color: Colors.grey.shade400, width: 1.5),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: ShapeWidget(
                    code: shapes[i],
                    color: color,
                    size: shapeSize,
                    rotation: rotations != null && i < rotations!.length
                        ? rotations![i].toDouble()
                        : 0,
                  ),
                ),
                if (i < shapes.length - 1)
                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 8),
                    child: Icon(
                      Icons.arrow_forward,
                      color: Colors.grey.shade600,
                      size: 24,
                    ),
                  ),
              ],
              // Tanda panah sebelum kotak ?
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 8),
                child: Icon(
                  Icons.arrow_forward,
                  color: Colors.grey.shade600,
                  size: 24,
                ),
              ),
              // KOTAK TANDA TANYA
              Container(
                width: shapeSize + 12,
                height: shapeSize + 12,
                padding: const EdgeInsets.all(6),
                decoration: BoxDecoration(
                  color: Colors.amber.shade50,
                  border: Border.all(color: Colors.amber.shade700, width: 2),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Center(
                  child: Text(
                    '?',
                    style: TextStyle(
                      fontSize: shapeSize * 0.45,
                      fontWeight: FontWeight.bold,
                      color: Colors.amber.shade800,
                    ),
                  ),
                ),
              ),
            ],
          ),
      ],
    );
  }
}

// ============================================================================
// MATRIKS FIGURAL WIDGET
// ============================================================================

class MatriksFiguralWidget extends StatelessWidget {
  final List<List<String>> grid;
  final Color color;
  final double cellSize;
  final List<String>? choices;

  const MatriksFiguralWidget({
    super.key,
    required this.grid,
    this.color = Colors.black87,
    this.cellSize = 50,
    this.choices,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text(
          'Lengkapi pola matriks berikut:',
          style: TextStyle(
            fontSize: 14,
            fontWeight: FontWeight.w500,
            color: Colors.grey.shade700,
          ),
        ),
        const SizedBox(height: 16),
        // Tampilkan matriks 3x3
        Column(
          children: [
            for (int row = 0; row < grid.length; row++)
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  for (int col = 0; col < grid[row].length; col++) ...[
                    Container(
                      width: cellSize + 8,
                      height: cellSize + 8,
                      margin: const EdgeInsets.all(2),
                      decoration: BoxDecoration(
                        color: Colors.white,
                        border: Border.all(
                          color: Colors.grey.shade400,
                          width: 1.5,
                        ),
                        borderRadius: BorderRadius.circular(6),
                      ),
                      child: Center(
                        child: ShapeWidget(
                          code: grid[row][col],
                          color: color,
                          size: cellSize,
                        ),
                      ),
                    ),
                  ],
                ],
              ),
          ],
        ),
      ],
    );
  }
}

// ============================================================================
// BAYANGAN FIGURAL WIDGET
// ============================================================================

class BayanganFiguralWidget extends StatelessWidget {
  final String originalShape;
  final List<String> options;
  final Color color;
  final double shapeSize;

  const BayanganFiguralWidget({
    super.key,
    required this.originalShape,
    required this.options,
    this.color = Colors.black87,
    this.shapeSize = 48,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            // Benda asli
            Column(
              children: [
                Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    border: Border.all(color: Colors.black87, width: 2),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: ShapeWidget(
                    code: originalShape,
                    color: color,
                    size: shapeSize,
                  ),
                ),
                const SizedBox(height: 4),
                const Text('Benda', style: TextStyle(fontSize: 12)),
              ],
            ),
            const SizedBox(width: 30),
            // Tanda tanya
            Column(
              children: [
                Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: Colors.grey.shade100,
                    border: Border.all(color: Colors.grey, width: 2),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Icon(Icons.help, color: Colors.grey, size: shapeSize),
                ),
                const SizedBox(height: 4),
                const Text('?', style: TextStyle(fontSize: 12)),
              ],
            ),
          ],
        ),
      ],
    );
  }
}

// ============================================================================
// FIGURAL QUESTION WIDGET — Widget utama
// ============================================================================

class FiguralQuestionWidget extends StatelessWidget {
  final FiguralData data;
  final Color color;
  final double shapeSize;

  const FiguralQuestionWidget({
    super.key,
    required this.data,
    this.color = Colors.black87,
    this.shapeSize = 48,
  });

  @override
  Widget build(BuildContext context) {
    switch (data.type) {
      case FiguralType.deret:
        final seq = List<String>.from(data.sequence);
        // Highlight last 2 shapes as "blanks to answer"
        final highlightIdx = seq.length - 2;
        return DeretFiguralWidget(
          shapes: seq,
          color: color,
          shapeSize: shapeSize,
          answerIndex: highlightIdx >= 0 ? highlightIdx : null,
          choices: data.answerShapeList.isNotEmpty ? data.answerShapeList : null,
        );

      case FiguralType.rotasi:
        final seq = List<String>.from(data.sequence);
        return RotasiFiguralWidget(
          shapes: seq,
          color: color,
          shapeSize: shapeSize,
          choices: data.answerShapeList.isNotEmpty ? data.answerShapeList : null,
        );

      case FiguralType.matriks:
        if (data.gridData == null) return const SizedBox();
        return MatriksFiguralWidget(
          grid: data.gridData!,
          color: color,
          cellSize: shapeSize,
          choices: data.answerShapeList.isNotEmpty ? data.answerShapeList : null,
        );

      case FiguralType.bayangan:
        if (data.sequence.isEmpty) return const SizedBox();
        return BayanganFiguralWidget(
          originalShape: data.sequence.first,
          options: data.answerShapeList,
          color: color,
          shapeSize: shapeSize,
        );
    }
  }
}

FiguralData? parseFiguralData(String? jsonStr) {
  if (jsonStr == null || jsonStr.isEmpty) return null;
  try {
    if (!jsonStr.trim().startsWith('{')) return null;
    final Map<String, dynamic> decoded = jsonDecode(jsonStr);
    return FiguralData.fromJson(decoded);
  } catch (_) {
    return null;
  }
}
