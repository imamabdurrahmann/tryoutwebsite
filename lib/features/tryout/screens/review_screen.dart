import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../../core/constants/app_constants.dart';
import '../../../data/models/question.dart';
import '../../../providers/tryout_provider.dart';
import '../../../providers/questions_provider.dart';
import '../../../core/theme/app_theme.dart';
import '../widgets/review_question_card.dart';

enum ReviewFilter { all, correct, wrong, unanswered }

class ReviewScreen extends ConsumerStatefulWidget {
  final String sessionId;

  const ReviewScreen({super.key, required this.sessionId});

  @override
  ConsumerState<ReviewScreen> createState() => _ReviewScreenState();
}

class _ReviewScreenState extends ConsumerState<ReviewScreen> {
  ReviewFilter _filter = ReviewFilter.all;
  String _categoryFilter = 'Semua'; // 'Semua', 'TWK', 'TIU', 'TKP'

  @override
  Widget build(BuildContext context) {
    final sessionAsync = ref.watch(sessionDetailProvider(widget.sessionId));
    final theme = Theme.of(context);

    return Scaffold(
      backgroundColor: theme.scaffoldBackgroundColor,
      appBar: AppBar(
        backgroundColor: theme.appBarTheme.backgroundColor,
        title: const Text('Pembahasan Ujian'),
        automaticallyImplyLeading: false,
        actions: [
          IconButton(
            icon: const Icon(Icons.close),
            onPressed: () => Navigator.of(context).pop(),
          ),
        ],
      ),
      body: sessionAsync.when(
        data: (session) {
          if (session == null) {
            return const Center(child: Text('Data tidak ditemukan'));
          }

          return Column(
            children: [
              // ===== Filter Chips =====
              _buildFilterChips(context),

              // ===== Question List =====
              Expanded(
                child: FutureBuilder(
                  future: _loadQuestionsForReview(ref, session.packageType),
                  builder: (context, snapshot) {
                    if (snapshot.connectionState == ConnectionState.waiting) {
                      return const Center(child: CircularProgressIndicator());
                    }

                    final questions = snapshot.data ?? [];
                    final answers = session.answers;

                    if (questions.isEmpty) {
                      return const Center(
                          child: Text('Soal tidak ditemukan untuk review'));
                    }

                    // Filter questions
                    final filtered = _applyFilter(questions, answers);
                    if (filtered.isEmpty) {
                      return _buildEmptyFilter(context);
                    }

                    // Build with original indices
                    return ListView.builder(
                      padding: const EdgeInsets.all(16),
                      itemCount: filtered.length,
                      itemBuilder: (context, index) {
                        final q = filtered[index];
                        final userAnswer = answers[q.questionId];
                        // Find original index in full question list
                        final origIndex = questions.indexWhere(
                            (question) => question.questionId == q.questionId);
                        return ReviewQuestionCard(
                          question: q,
                          userAnswer: userAnswer,
                          questionIndex: origIndex >= 0 ? origIndex : index,
                        );
                      },
                    );
                  },
                ),
              ),
            ],
          );
        },
        loading: () => const Center(child: CircularProgressIndicator()),
        error: (e, _) => Center(child: Text('Error: $e')),
      ),
    );
  }

  Widget _buildFilterChips(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      decoration: BoxDecoration(
        color: Theme.of(context).cardColor,
        border: Border(
          bottom: BorderSide(color: Colors.grey.shade200),
        ),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Status filter row
          SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            child: Row(
              children: [
                _buildChip(context, 'Semua', ReviewFilter.all, Icons.list),
                const SizedBox(width: 8),
                _buildChip(context, 'Benar', ReviewFilter.correct, Icons.check_circle,
                    AppTheme.successGreen),
                const SizedBox(width: 8),
                _buildChip(context, 'Salah', ReviewFilter.wrong, Icons.cancel,
                    AppTheme.errorRed),
                const SizedBox(width: 8),
                _buildChip(
                    context, 'Kosong', ReviewFilter.unanswered, Icons.remove_circle,
                    Colors.grey),
              ],
            ),
          ),
          const SizedBox(height: 8),
          // Category filter row
          SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            child: Row(
              children: ['Semua', 'TWK', 'TIU', 'TKP'].map((cat) {
                final isSelected = _categoryFilter == cat;
                final catColor = cat == 'TWK' ? AppTheme.secondaryBlue
                    : cat == 'TIU' ? AppTheme.warningOrange
                    : cat == 'TKP' ? AppTheme.successGreen
                    : AppTheme.primaryRed;
                return Padding(
                  padding: const EdgeInsets.only(right: 8),
                  child: GestureDetector(
                    onTap: () => setState(() => _categoryFilter = cat),
                    child: AnimatedContainer(
                      duration: const Duration(milliseconds: 200),
                      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                      decoration: BoxDecoration(
                        color: isSelected ? catColor.withAlpha(20) : Colors.grey.shade100,
                        borderRadius: BorderRadius.circular(16),
                        border: Border.all(
                          color: isSelected ? catColor.withAlpha(80) : Colors.transparent,
                        ),
                      ),
                      child: Text(
                        cat,
                        style: TextStyle(
                          color: isSelected ? catColor : Colors.grey.shade600,
                          fontSize: 11,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                    ),
                  ),
                );
              }).toList(),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildChip(
    BuildContext context,
    String label,
    ReviewFilter filter,
    IconData icon, [
    Color? color,
  ]) {
    final isSelected = _filter == filter;
    final chipColor = color ?? AppTheme.primaryRed;

    return GestureDetector(
      onTap: () => setState(() => _filter = filter),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
        decoration: BoxDecoration(
          color: isSelected
              ? chipColor.withAlpha(20)
              : Colors.grey.shade100,
          borderRadius: BorderRadius.circular(20),
          border: Border.all(
            color: isSelected
                ? chipColor.withAlpha(80)
                : Colors.transparent,
            width: 1.5,
          ),
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              icon,
              size: 14,
              color: isSelected ? chipColor : Colors.grey.shade600,
            ),
            const SizedBox(width: 4),
            Text(
              label,
              style: TextStyle(
                color: isSelected ? chipColor : Colors.grey.shade600,
                fontSize: 12,
                fontWeight: FontWeight.w600,
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildEmptyFilter(BuildContext context) {
    String message;
    IconData icon;
    switch (_filter) {
      case ReviewFilter.correct:
        message = 'Belum ada soal yang dijawab dengan benar';
        icon = Icons.check_circle_outline;
        break;
      case ReviewFilter.wrong:
        message = 'Tidak ada soal yang salah';
        icon = Icons.cancel_outlined;
        break;
      case ReviewFilter.unanswered:
        message = 'Semua soal sudah dijawab';
        icon = Icons.task_alt;
        break;
      default:
        message = 'Tidak ada soal';
        icon = Icons.help_outline;
    }

    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(icon, size: 48, color: Colors.grey.shade400),
          const SizedBox(height: 12),
          Text(
            message,
            style: TextStyle(color: Colors.grey.shade600, fontSize: 14),
          ),
        ],
      ),
    );
  }

  Future<List<Question>> _loadQuestionsForReview(
    WidgetRef ref,
    String packageType,
  ) async {
    final repo = ref.read(questionRepositoryProvider);

    // Tangkap paket 1, 2, atau 3
    final packageNum = AppConstants.extractPackageNumber(packageType);
    repo.setPackage(packageNum);

    // Tangkap jenis tes
    if (packageType.startsWith('FULL')) {
      return repo.getAllQuestions();
    } else if (packageType.startsWith('TWK_ONLY')) {
      return repo.getQuestionsByCategory('TWK');
    } else if (packageType.startsWith('TIU_ONLY')) {
      return repo.getQuestionsByCategory('TIU');
    } else if (packageType.startsWith('TKP_ONLY')) {
      return repo.getQuestionsByCategory('TKP');
    } else {
      repo.setPackage('1');
      return repo.getAllQuestions();
    }
  }

  List<Question> _applyFilter(
    List<Question> questions,
    Map<String, String> answers,
  ) {
    var filtered = questions;

    // Category filter
    if (_categoryFilter != 'Semua') {
      filtered = filtered.where((q) => q.category == _categoryFilter).toList();
    }

    // Status filter
    switch (_filter) {
      case ReviewFilter.correct:
        return filtered
            .where((q) => answers[q.questionId] == q.answer)
            .toList();
      case ReviewFilter.wrong:
        return filtered
            .where((q) =>
                answers[q.questionId] != null &&
                answers[q.questionId]!.isNotEmpty &&
                answers[q.questionId] != q.answer)
            .toList();
      case ReviewFilter.unanswered:
        return filtered
            .where((q) => answers[q.questionId] == null || answers[q.questionId]!.isEmpty)
            .toList();
      default:
        return filtered;
    }
  }
}