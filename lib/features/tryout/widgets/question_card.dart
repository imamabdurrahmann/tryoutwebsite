import 'dart:convert';

import 'package:flutter/material.dart';
import '../../../data/models/question.dart';
import '../../../core/theme/app_theme.dart';
import '../../../core/utils/app_utils.dart';
import 'figural_question_widget.dart';

class QuestionCard extends StatefulWidget {
  final Question question;
  final String? selectedAnswer;
  final ValueChanged<String> onAnswerSelected;
  final bool showAnswer;
  final bool isPracticeMode;

  const QuestionCard({
    super.key,
    required this.question,
    required this.selectedAnswer,
    required this.onAnswerSelected,
    this.showAnswer = false,
    this.isPracticeMode = false,
  });

  @override
  State<QuestionCard> createState() => _QuestionCardState();
}

class _QuestionCardState extends State<QuestionCard> {
  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final bool isReallyFigural = widget.question.isFigural || 
        widget.question.subcategory.toLowerCase() == 'figural' || 
        (widget.question.figuralData != null && widget.question.figuralData!.isNotEmpty);

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Difficulty Badge
        if (widget.question.difficulty.isNotEmpty) ...[
          _buildDifficultyBadge(),
          const SizedBox(height: 12),
        ],

        // Subcategory
        Text(
          widget.question.subcategory,
          style: theme.textTheme.bodySmall?.copyWith(
            color: AppTheme.primaryRed,
            fontWeight: FontWeight.w600,
          ),
        ),
        const SizedBox(height: 8),

        // Question Text
        Container(
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(
            color: theme.cardColor,
            borderRadius: BorderRadius.circular(12),
            boxShadow: [
              BoxShadow(
                color: Colors.black.withAlpha(13),
                blurRadius: 4,
                offset: const Offset(0, 2),
              ),
            ],
          ),
          child: Text(
            widget.question.questionText,
            style: theme.textTheme.bodyLarge?.copyWith(
              height: 1.5,
            ),
          ),
        ),
        const SizedBox(height: 20),

        // Figural question visualization
        if (isReallyFigural && widget.question.figuralData != null) ...[
          _buildFiguralDisplay(context),
        ] else ...[
          // Answer Options
          ...List.generate(
            widget.question.options.length,
            (index) => _buildOptionItem(
              context,
              widget.question.getOptionLabel(index),
              widget.question.options[index],
            ),
          ),
        ],

        // Explanation (shown immediately in practice mode)
        if (widget.showAnswer && widget.selectedAnswer != null) ...[
          const SizedBox(height: 20),
          _buildExplanation(context),
        ],
      ],
    );
  }

  Widget _buildDifficultyBadge() {
    Color color;
    String label;

    switch (widget.question.difficulty) {
      case 'easy':
        color = AppTheme.successGreen;
        label = 'Mudah';
        break;
      case 'medium':
        color = AppTheme.warningOrange;
        label = 'Sedang';
        break;
      case 'hard':
        color = AppTheme.errorRed;
        label = 'Sulit';
        break;
      default:
        color = Colors.grey;
        label = '';
    }

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
      decoration: BoxDecoration(
        color: color.withAlpha(26),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: color.withAlpha(77)),
      ),
      child: Text(
        label,
        style: TextStyle(
          color: color,
          fontSize: 11,
          fontWeight: FontWeight.bold,
        ),
      ),
    );
  }

  Widget _buildFiguralDisplay(BuildContext context) {
    // ✅ Parse JSON string to FiguralData
    final rawJson = widget.question.figuralData;
    if (rawJson == null || rawJson.isEmpty) return const SizedBox();

    try {
      final json = jsonDecode(rawJson) as Map<String, dynamic>;
      final data = FiguralData.fromJson(json);
      return Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Visualisasi bentuk
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: Colors.blue.shade50,
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: Colors.blue.shade200),
            ),
            child: FiguralQuestionWidget(
              data: data,
              color: Colors.black87,
              shapeSize: 44,
            ),
          ),
          const SizedBox(height: 16),
          // Pilihan jawaban A-E
          ..._buildFiguralAnswerOptions(context, data),
        ],
      );
    } catch (e) {
      return Container(
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: Colors.red.shade50,
          borderRadius: BorderRadius.circular(8),
        ),
        child: Text(
          'Data figural error',
          style: TextStyle(color: Colors.red.shade700, fontSize: 12),
        ),
      );
    }
  }

  List<Widget> _buildFiguralAnswerOptions(BuildContext context, FiguralData data) {
    final List<Widget> options = [];
    final choices = data.answerShapeList;
    final correctIndex = data.correctIndex;

    for (int i = 0; i < 5; i++) {
      final label = ['A', 'B', 'C', 'D', 'E'][i];
      final isSelected = widget.selectedAnswer == label;
      final isCorrectOption = i == correctIndex;

      Color borderColor;
      Color bgColor;

      if (widget.showAnswer) {
        if (isCorrectOption) {
          borderColor = AppTheme.successGreen;
          bgColor = AppTheme.successGreen.withAlpha(26);
        } else if (isSelected && !isCorrectOption) {
          borderColor = AppTheme.errorRed;
          bgColor = AppTheme.errorRed.withAlpha(26);
        } else {
          borderColor = Colors.grey.shade300;
          bgColor = Colors.transparent;
        }
      } else {
        borderColor = isSelected ? AppTheme.primaryRed : Colors.grey.shade300;
        bgColor = isSelected ? AppTheme.primaryRed.withAlpha(20) : Colors.transparent;
      }

      options.add(
        Padding(
          padding: const EdgeInsets.only(bottom: 8),
          child: Material(
            color: Colors.transparent,
            child: InkWell(
              onTap: () {
                      // ✅ Toggle: tap same option to unselect, tap different to select
                      if (widget.selectedAnswer == label) {
                        widget.onAnswerSelected('');
                      } else {
                        widget.onAnswerSelected(label);
                      }
                    },
              borderRadius: BorderRadius.circular(12),
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 200),
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
                decoration: BoxDecoration(
                  color: bgColor,
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(
                    color: borderColor,
                    width: isSelected || isCorrectOption ? 2 : 1,
                  ),
                ),
                child: Row(
                  children: [
                    Container(
                      width: 32,
                      height: 32,
                      decoration: BoxDecoration(
                        color: isSelected || isCorrectOption
                            ? borderColor.withAlpha(51)
                            : Colors.grey.shade100,
                        shape: BoxShape.circle,
                      ),
                      child: Center(
                        child: Text(
                          label,
                          style: TextStyle(
                            fontWeight: FontWeight.bold,
                            color: isSelected || isCorrectOption
                                ? borderColor
                                : Colors.grey.shade600,
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(width: 12),
                    // Gambar bentuk
                    if (i < choices.length)
                      ShapeWidget(
                        code: choices[i],
                        color: AppUtils.parseColor(
                          choices[i],
                          Theme.of(context).brightness == Brightness.dark ? Colors.white : Colors.black87,
                        ),
                        size: 36,
                      ),
                    const Spacer(),
                    if (isCorrectOption && widget.showAnswer)
                      const Icon(Icons.check_circle, color: AppTheme.successGreen, size: 24),
                    if (isSelected && !isCorrectOption && widget.showAnswer)
                      const Icon(Icons.cancel, color: AppTheme.errorRed, size: 24),
                  ],
                ),
              ),
            ),
          ),
        ),
      );
    }
    return options;
  }

  Widget _buildOptionItem(BuildContext context, String label, String text) {
    final isSelected = widget.selectedAnswer == label;
    final isCorrect = widget.showAnswer && widget.question.answer == label;
    final isWrong = widget.showAnswer && widget.selectedAnswer == label && !isCorrect;

    Color borderColor;
    Color bgColor;

    if (widget.showAnswer) {
      if (isCorrect) {
        borderColor = AppTheme.successGreen;
        bgColor = AppTheme.successGreen.withAlpha(26);
      } else if (isWrong) {
        borderColor = AppTheme.errorRed;
        bgColor = AppTheme.errorRed.withAlpha(26);
      } else {
        borderColor = Colors.grey.shade300;
        bgColor = Colors.transparent;
      }
    } else {
      borderColor = isSelected ? AppTheme.primaryRed : Colors.grey.shade300;
      bgColor = isSelected ? AppTheme.primaryRed.withAlpha(20) : Colors.transparent;
    }

    return Padding(
      padding: const EdgeInsets.only(bottom: 10),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        child: Material(
          color: Colors.transparent,
          child: InkWell(
            onTap: () {
                    // ✅ Toggle: tap same option to unselect, tap different to select
                    if (widget.selectedAnswer == label) {
                      widget.onAnswerSelected('');
                    } else {
                      widget.onAnswerSelected(label);
                    }
                  },
            borderRadius: BorderRadius.circular(12),
            child: AnimatedContainer(
              duration: const Duration(milliseconds: 200),
              padding: const EdgeInsets.all(14),
              decoration: BoxDecoration(
                color: bgColor,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(
                  color: borderColor,
                  width: isSelected || isCorrect || isWrong ? 2 : 1,
                ),
              ),
              child: Row(
                children: [
                  Container(
                    width: 32,
                    height: 32,
                    decoration: BoxDecoration(
                      color: isSelected || isCorrect || isWrong
                          ? borderColor.withAlpha(51)
                          : Colors.grey.shade100,
                      shape: BoxShape.circle,
                    ),
                    child: Center(
                      child: Text(
                        label,
                        style: TextStyle(
                          fontWeight: FontWeight.bold,
                          color: isSelected || isCorrect || isWrong
                              ? borderColor
                              : Colors.grey.shade600,
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Text(
                      text,
                      style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                            color: isSelected || isCorrect
                                ? (isWrong ? AppTheme.errorRed : null)
                                : null,
                          ),
                    ),
                  ),
                  if (isCorrect && widget.showAnswer)
                    const Icon(Icons.check_circle, color: AppTheme.successGreen, size: 24),
                  if (isWrong)
                    const Icon(Icons.cancel, color: AppTheme.errorRed, size: 24),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildExplanation(BuildContext context) {
    final theme = Theme.of(context);
    final isCorrect = widget.selectedAnswer == widget.question.answer;

    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: isCorrect
            ? AppTheme.successGreen.withAlpha(26)
            : AppTheme.errorRed.withAlpha(26),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(
          color: isCorrect
              ? AppTheme.successGreen.withAlpha(77)
              : AppTheme.errorRed.withAlpha(77),
        ),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(
                isCorrect ? Icons.check_circle : Icons.cancel,
                color: isCorrect ? AppTheme.successGreen : AppTheme.errorRed,
                size: 20,
              ),
              const SizedBox(width: 8),
              Text(
                isCorrect ? 'Benar!' : 'Kurang Tepat',
                style: TextStyle(
                  color: isCorrect ? AppTheme.successGreen : AppTheme.errorRed,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Text(
            'Pembahasan:',
            style: theme.textTheme.titleSmall?.copyWith(
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 4),
          Text(
            widget.question.explanation,
            style: theme.textTheme.bodyMedium?.copyWith(height: 1.5),
          ),
        ],
      ),
    );
  }
}