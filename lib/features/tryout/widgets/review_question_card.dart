import 'package:flutter/material.dart';
import '../../../core/theme/app_theme.dart';
import '../../../data/models/question.dart';
import '../../../core/utils/app_utils.dart';
import 'figural_question_widget.dart';

/// Widget kartu review untuk satu soal.
/// Menampilkan soal, opsi berwarna (hijau=benar, merah=salah),
/// dan kotak pembahasan dengan ikon lightbulb.
class ReviewQuestionCard extends StatelessWidget {
  final Question question;
  final String? userAnswer;
  final int questionIndex;
  final bool isFlagged;

  const ReviewQuestionCard({
    super.key,
    required this.question,
    required this.questionIndex,
    this.userAnswer,
    this.isFlagged = false,
  });

  bool get isCorrect => userAnswer == question.answer;
  bool get isUnanswered => userAnswer == null || userAnswer!.isEmpty;

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.only(bottom: 16),
      elevation: 0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
        side: BorderSide(color: Colors.grey.shade200),
      ),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // ===== Header: Kategori + Status =====
            _buildHeader(context),
            const SizedBox(height: 12),

            // ===== Pertanyaan =====
            if ((question.isFigural || question.subcategory.toLowerCase() == 'figural' || (question.figuralData != null && question.figuralData!.isNotEmpty)) && question.figuralData != null)
              _buildFiguralContent(context)
            else
              _buildTextContent(context),

            const SizedBox(height: 16),

            // ===== Opsi Jawaban =====
            if ((question.isFigural || question.subcategory.toLowerCase() == 'figural' || (question.figuralData != null && question.figuralData!.isNotEmpty)) && question.figuralData != null)
              _buildFiguralOptions(context)
            else
              _buildTextOptions(context),

            const SizedBox(height: 16),

            // ===== Pembahasan =====
            _buildExplanation(context),
          ],
        ),
      ),
    );
  }

  Widget _buildHeader(BuildContext context) {
    final statusColor = isUnanswered
        ? Colors.grey
        : isCorrect
            ? AppTheme.successGreen
            : AppTheme.errorRed;

    final statusText = isUnanswered
        ? 'Tidak Dijawab'
        : isCorrect
            ? 'Benar'
            : 'Salah';

    final statusIcon = isUnanswered
        ? Icons.remove_circle_outline
        : isCorrect
            ? Icons.check_circle
            : Icons.cancel;

    final categoryColor = _getCategoryColor(question.category);

    return Row(
      children: [
        // No. Soal
        Container(
          width: 36,
          height: 36,
          decoration: BoxDecoration(
            color: categoryColor.withAlpha(20),
            shape: BoxShape.circle,
            border: Border.all(color: categoryColor.withAlpha(50)),
          ),
          child: Center(
            child: Text(
              '${questionIndex + 1}',
              style: TextStyle(
                color: categoryColor,
                fontWeight: FontWeight.bold,
                fontSize: 13,
              ),
            ),
          ),
        ),
        const SizedBox(width: 8),

        // Kategori + Subkategori
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
          decoration: BoxDecoration(
            color: categoryColor.withAlpha(15),
            borderRadius: BorderRadius.circular(8),
          ),
          child: Text(
            question.category,
            style: TextStyle(
              color: categoryColor,
              fontSize: 11,
              fontWeight: FontWeight.bold,
            ),
          ),
        ),
        const SizedBox(width: 6),
        Expanded(
          child: Text(
            question.subcategory,
            style: TextStyle(color: Colors.grey.shade500, fontSize: 11),
            overflow: TextOverflow.ellipsis,
          ),
        ),

        // Status badge
        if (isFlagged)
          Container(
            margin: const EdgeInsets.only(left: 4),
            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 5),
            decoration: BoxDecoration(
              color: AppTheme.catFlagged.withAlpha(15),
              borderRadius: BorderRadius.circular(20),
              border: Border.all(color: AppTheme.catFlagged.withAlpha(40)),
            ),
            child: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Icon(Icons.flag, color: AppTheme.catFlagged, size: 14),
                const SizedBox(width: 4),
                Text(
                  'Ragu',
                  style: TextStyle(
                    color: AppTheme.catFlagged,
                    fontSize: 11,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ],
            ),
          )
        else
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
            decoration: BoxDecoration(
              color: statusColor.withAlpha(15),
              borderRadius: BorderRadius.circular(20),
              border: Border.all(color: statusColor.withAlpha(40)),
            ),
            child: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Icon(statusIcon, color: statusColor, size: 14),
                const SizedBox(width: 4),
                Text(
                  statusText,
                  style: TextStyle(
                    color: statusColor,
                    fontSize: 11,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ],
            ),
          ),
      ],
    );
  }

  Widget _buildTextContent(BuildContext context) {
    return Text(
      question.questionText,
      style: Theme.of(context).textTheme.bodyMedium?.copyWith(
            height: 1.6,
            fontWeight: FontWeight.w500,
          ),
    );
  }

  Widget _buildFiguralContent(BuildContext context) {
    final data = parseFiguralData(question.figuralData);
    if (data == null) {
      return Container(
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: Colors.grey.shade100,
          borderRadius: BorderRadius.circular(12),
        ),
        child: const Text('Soal figural tidak dapat dimuat.'),
      );
    }

    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.blue.shade50,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: Colors.blue.shade100),
      ),
      child: Center(
        child: FiguralQuestionWidget(
          data: data,
          color: Colors.black87,
          shapeSize: 44,
        ),
      ),
    );
  }

  Widget _buildTextOptions(BuildContext context) {
    final isTkp = question.category == 'TKP';
    final labels = ['A', 'B', 'C', 'D', 'E'];

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: List.generate(question.options.length, (index) {
        final label = labels[index];
        final isUserAnswer = userAnswer == label;
        final isCorrectAnswer = question.answer == label;

        // Tentukan warna
        Color? highlightColor;
        String? indicator;

        if (isCorrectAnswer) {
          highlightColor = AppTheme.successGreen;
          indicator = 'correct';
        } else if (isUserAnswer) {
          highlightColor = AppTheme.errorRed;
          indicator = 'wrong';
        }

        final bgColor = highlightColor?.withAlpha(15) ?? Colors.grey.shade50;
        final borderColor = highlightColor?.withAlpha(50) ?? Colors.transparent;

        return Padding(
          padding: const EdgeInsets.only(bottom: 6),
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
            decoration: BoxDecoration(
              color: bgColor,
              borderRadius: BorderRadius.circular(10),
              border: Border.all(color: borderColor, width: 1.5),
            ),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Label
                Container(
                  width: 26,
                  height: 26,
                  decoration: BoxDecoration(
                    color: highlightColor?.withAlpha(25) ?? Colors.grey.shade200,
                    shape: BoxShape.circle,
                  ),
                  child: Center(
                    child: Text(
                      label,
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.bold,
                        color: highlightColor ?? Colors.grey.shade600,
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 10),

                // Teks opsi
                Expanded(
                  child: Text(
                    question.options[index],
                    style: TextStyle(
                      fontSize: 13,
                      height: 1.4,
                      color: highlightColor ?? Colors.black87,
                      fontWeight: isUserAnswer || isCorrectAnswer
                          ? FontWeight.w600
                          : FontWeight.normal,
                    ),
                  ),
                ),

                // Skor TKP
                if (isTkp) ...[
                  const SizedBox(width: 8),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                    decoration: BoxDecoration(
                      color: Colors.grey.shade100,
                      borderRadius: BorderRadius.circular(6),
                    ),
                    child: Text(
                      '${5 - index} poin',
                      style: TextStyle(
                        color: Colors.grey.shade600,
                        fontSize: 10,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ),
                ],

                // Indikator
                const SizedBox(width: 6),
                if (indicator == 'correct')
                  const Icon(Icons.check_circle,
                      color: AppTheme.successGreen, size: 18)
                else if (indicator == 'wrong')
                  const Icon(Icons.close, color: AppTheme.errorRed, size: 18),
              ],
            ),
          ),
        );
      }),
    );
  }

  Widget _buildFiguralOptions(BuildContext context) {
    final data = parseFiguralData(question.figuralData);
    if (data == null) return const SizedBox.shrink();

    final choices = data.answerShapeList;
    final labels = ['A', 'B', 'C', 'D', 'E'];
    final correctIndex = data.correctIndex;

    return Wrap(
      spacing: 8,
      runSpacing: 8,
      children: List.generate(
        choices.length < 5 ? choices.length : 5,
        (index) {
          final label = labels[index];
          final isCorrectOption = index == correctIndex;
          final isUserAnswer = userAnswer == label;

          Color? color;
          if (isCorrectOption) {
            color = AppTheme.successGreen;
          } else if (isUserAnswer) {
            color = AppTheme.errorRed;
          }

          return Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
            decoration: BoxDecoration(
              color: color?.withAlpha(15) ?? Colors.grey.shade50,
              borderRadius: BorderRadius.circular(10),
              border: Border.all(color: color?.withAlpha(50) ?? Colors.transparent),
            ),
            child: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Container(
                  width: 24,
                  height: 24,
                  decoration: BoxDecoration(
                    color: color?.withAlpha(25) ?? Colors.grey.shade200,
                    shape: BoxShape.circle,
                  ),
                  child: Center(
                    child: Text(
                      label,
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.bold,
                        color: color ?? Colors.grey.shade600,
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 8),
                ShapeWidget(
                  code: choices[index],
                  color: AppUtils.parseColor(choices[index], color ?? Colors.black54),
                  size: 32,
                ),
                const SizedBox(width: 6),
                if (isCorrectOption)
                  const Icon(Icons.check_circle,
                      color: AppTheme.successGreen, size: 16)
                else if (isUserAnswer && !isCorrectOption)
                  const Icon(Icons.close,
                      color: AppTheme.errorRed, size: 16),
              ],
            ),
          );
        },
      ),
    );
  }

  Widget _buildExplanation(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: Colors.amber.shade50,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: Colors.amber.shade200),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            padding: const EdgeInsets.all(6),
            decoration: BoxDecoration(
              color: Colors.amber.shade100,
              shape: BoxShape.circle,
            ),
            child: Icon(
              Icons.lightbulb,
              color: Colors.amber.shade800,
              size: 18,
            ),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Pembahasan',
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    color: Colors.amber.shade900,
                    fontSize: 13,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  question.explanation,
                  style: TextStyle(
                    color: Colors.amber.shade900,
                    fontSize: 12,
                    height: 1.5,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }





  Color _getCategoryColor(String category) {
    switch (category) {
      case 'TWK':
        return AppTheme.secondaryBlue;
      case 'TIU':
        return AppTheme.warningOrange;
      case 'TKP':
        return AppTheme.successGreen;
      default:
        return AppTheme.primaryRed;
    }
  }
}