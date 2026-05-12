import 'package:flutter/material.dart';
import '../../../data/models/question.dart';
import '../../../core/theme/app_theme.dart';

class QuestionNavBar extends StatefulWidget {
  final int totalQuestions;
  final int currentIndex;
  final Map<String, String> answers;
  final Set<String> flagged;
  final Set<String> visited;
  final List<Question> questions;
  final ValueChanged<int> onQuestionTap;

  const QuestionNavBar({
    super.key,
    required this.totalQuestions,
    required this.currentIndex,
    required this.answers,
    required this.flagged,
    required this.visited,
    required this.questions,
    required this.onQuestionTap,
  });

  @override
  State<QuestionNavBar> createState() => _QuestionNavBarState();
}

class _QuestionNavBarState extends State<QuestionNavBar> {
  bool _isExpanded = false;

  @override
  Widget build(BuildContext context) {
    final answeredCount = widget.answers.length;
    final visitedCount = widget.visited.length;
    final unansweredVisited = visitedCount - answeredCount;
    final notVisited = widget.totalQuestions - visitedCount;

    return AnimatedContainer(
      duration: const Duration(milliseconds: 300),
      height: _isExpanded ? 380 : 60,
      decoration: BoxDecoration(
        color: Theme.of(context).cardColor,
        boxShadow: [
          BoxShadow(
            color: Colors.black.withAlpha(26),
            blurRadius: 8,
            offset: const Offset(0, -2),
          ),
        ],
      ),
      child: Column(
        children: [
          // Toggle Button
          InkWell(
            onTap: () => setState(() => _isExpanded = !_isExpanded),
            child: Container(
              height: 60,
              padding: const EdgeInsets.symmetric(horizontal: 16),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  // Summary (BKN 4-color mini indicators)
                  Row(
                    children: [
                      _buildMiniIndicator(AppTheme.catAnswered, '$answeredCount'),
                      const SizedBox(width: 10),
                      _buildMiniIndicator(AppTheme.catVisitedEmpty, '$unansweredVisited'),
                      const SizedBox(width: 10),
                      _buildMiniIndicator(AppTheme.catUnvisited, '$notVisited'),
                      const SizedBox(width: 10),
                      if (widget.flagged.isNotEmpty)
                        _buildMiniIndicator(AppTheme.catFlagged, '${widget.flagged.length}'),
                    ],
                  ),
                  // Arrow
                  AnimatedRotation(
                    duration: const Duration(milliseconds: 300),
                    turns: _isExpanded ? 0.5 : 0,
                    child: const Icon(Icons.keyboard_arrow_up),
                  ),
                ],
              ),
            ),
          ),

          // Question Grid + Legenda
          if (_isExpanded)
            SizedBox(
              height: 320,
              child: Column(
                children: [
                  // Grid
                  Expanded(
                    child: SingleChildScrollView(
                      padding: const EdgeInsets.fromLTRB(12, 8, 12, 4),
                      child: Wrap(
                        spacing: 8,
                        runSpacing: 8,
                        children: List.generate(
                          widget.totalQuestions,
                          (index) => _buildQuestionDot(context, index),
                        ),
                      ),
                    ),
                  ),
                  // Legenda Warna
                  _buildColorLegenda(context),
                ],
              ),
            ),
        ],
      ),
    );
  }

  Widget _buildMiniIndicator(Color color, String label) {
    return Row(
      children: [
        Container(
          width: 12,
          height: 12,
          decoration: BoxDecoration(
            color: color,
            shape: BoxShape.circle,
          ),
        ),
        const SizedBox(width: 4),
        Text(
          label,
          style: const TextStyle(fontSize: 12, color: Colors.grey),
        ),
      ],
    );
  }

  Widget _buildColorLegenda(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
      decoration: BoxDecoration(
        border: Border(top: BorderSide(color: Colors.grey.shade200)),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        children: [
          _legendaItem(AppTheme.catAnswered, 'Dijawab'),
          _legendaItem(AppTheme.catVisitedEmpty, 'Kosong'),
          _legendaItem(AppTheme.catFlagged, 'Ragu'),
          _legendaItem(AppTheme.catUnvisited, 'Blm Dlkungi'),
        ],
      ),
    );
  }

  Widget _legendaItem(Color color, String label) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        Container(
          width: 14,
          height: 14,
          decoration: BoxDecoration(
            color: color,
            borderRadius: BorderRadius.circular(3),
          ),
        ),
        const SizedBox(width: 4),
        Text(
          label,
          style: TextStyle(fontSize: 10, color: Colors.grey.shade600),
        ),
      ],
    );
  }

  Widget _buildQuestionDot(BuildContext context, int index) {
    if (index >= widget.questions.length) return const SizedBox();

    final q = widget.questions[index];
    final questionId = q.questionId;
    final isVisited = widget.visited.contains(questionId);
    final isAnswered = widget.answers.containsKey(questionId);
    final isFlagged = widget.flagged.contains(questionId);
    final isCurrent = index == widget.currentIndex;

    Color bgColor;
    Color borderColor;

    if (isCurrent) {
      bgColor = AppTheme.currentColor;
      borderColor = AppTheme.currentColor;
    } else if (isFlagged) {
      // Prioritas 1: Ragu (Kuning) — berlaku apapun kondisi jawaban
      bgColor = AppTheme.catFlagged;
      borderColor = AppTheme.catFlagged;
    } else if (isAnswered) {
      // Prioritas 2: Sudah dijawab (Hijau)
      bgColor = AppTheme.catAnswered;
      borderColor = AppTheme.catAnswered;
    } else if (isVisited) {
      // Prioritas 3: Dikunjungi tapi kosong (Merah)
      bgColor = AppTheme.catVisitedEmpty;
      borderColor = AppTheme.catVisitedEmpty;
    } else {
      // Belum dikunjungi (Abu-abu)
      bgColor = AppTheme.catUnvisited;
      borderColor = AppTheme.catUnvisited;
    }

    return GestureDetector(
      onTap: () => widget.onQuestionTap(index),
      child: Container(
        width: 36,
        height: 36,
        decoration: BoxDecoration(
          color: bgColor,
          borderRadius: BorderRadius.circular(8),
          border: Border.all(
            color: borderColor,
            width: isCurrent ? 2 : 1,
          ),
        ),
        child: Stack(
          children: [
            Center(
              child: Text(
                '${index + 1}',
                style: TextStyle(
                  color: isCurrent || isAnswered || isFlagged || isVisited
                      ? Colors.white
                      : Colors.grey.shade600,
                  fontWeight: FontWeight.bold,
                  fontSize: 12,
                ),
              ),
            ),
            if (isFlagged && !isCurrent)
              Positioned(
                top: 2,
                right: 2,
                child: Icon(
                  Icons.flag,
                  size: 10,
                  color: Colors.white,
                ),
              ),
          ],
        ),
      ),
    );
  }
}
