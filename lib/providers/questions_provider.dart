import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../data/repositories/question_repository.dart';
import '../data/models/question.dart';

final questionRepositoryProvider = Provider((ref) => QuestionRepository());

final allQuestionsProvider = FutureProvider<List<Question>>((ref) async {
  final repo = ref.watch(questionRepositoryProvider);
  return repo.getAllQuestions();
});

final questionsByCategoryProvider = FutureProvider.family<List<Question>, String>((ref, category) async {
  final repo = ref.watch(questionRepositoryProvider);
  return repo.getQuestionsByCategory(category);
});

final questionsBySubcategoryProvider = FutureProvider.family<List<Question>, String>((ref, subcategory) async {
  final repo = ref.watch(questionRepositoryProvider);
  return repo.getQuestionsBySubcategory(subcategory);
});

final practiceQuestionsProvider = FutureProvider.family<List<Question>, PracticeParams>((ref, params) async {
  final repo = ref.watch(questionRepositoryProvider);
  return repo.getPracticeQuestions(
    category: params.category,
    subcategory: params.subcategory,
  );
});

class PracticeParams {
  final String? category;
  final String? subcategory;

  const PracticeParams({this.category, this.subcategory});

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is PracticeParams &&
          runtimeType == other.runtimeType &&
          category == other.category &&
          subcategory == other.subcategory;

  @override
  int get hashCode => Object.hash(category, subcategory);
}
