import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import '../../../core/constants/app_constants.dart';
import '../../../core/theme/app_theme.dart';
import '../../../providers/questions_provider.dart';
import '../../../providers/tryout_provider.dart';

class PracticeScreen extends ConsumerStatefulWidget {
  const PracticeScreen({super.key});

  @override
  ConsumerState<PracticeScreen> createState() => _PracticeScreenState();
}

class _PracticeScreenState extends ConsumerState<PracticeScreen> {
  String? _selectedCategory;
  String? _selectedSubcategory;
  bool _isLoading = false;

  final List<String> _categories = ['TWK', 'TIU', 'TKP'];

  Map<String, List<String>> get _subcategoriesByCategory => {
        'TWK': AppConstants.twkSubcategories,
        'TIU': AppConstants.tiuSubcategories,
        'TKP': AppConstants.tkpSubcategories,
      };

  List<String> get _currentSubcategories =>
      _selectedCategory != null
          ? _subcategoriesByCategory[_selectedCategory] ?? []
          : [];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Latihan Per Subtopik'),
      ),
      body: Center(
        child: ConstrainedBox(
          constraints: const BoxConstraints(maxWidth: 900),
          child: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Info Card
            Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: AppTheme.secondaryBlue.withAlpha(26),
                borderRadius: BorderRadius.circular(12),
                border: Border.all(
                    color: AppTheme.secondaryBlue.withAlpha(77)),
              ),
              child: Row(
                children: [
                  const Icon(Icons.school,
                      color: AppTheme.secondaryBlue),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Text(
                      'Drill semua soal yang tersedia untuk subtopik yang dipilih. Jawaban benar langsung ditampilkan.',
                      style: TextStyle(
                        color: AppTheme.secondaryBlue,
                        fontSize: 13,
                      ),
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 24),

            // Category Selection
            Text(
              'Pilih Kategori',
              style: Theme.of(context).textTheme.titleSmall?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
            ),
            const SizedBox(height: 8),
            Wrap(
              spacing: 8,
              children: _categories.map((cat) {
                final isSelected = _selectedCategory == cat;
                return ChoiceChip(
                  label: Text(cat),
                  selected: isSelected,
                  onSelected: (selected) {
                    setState(() {
                      _selectedCategory = selected ? cat : null;
                      _selectedSubcategory = null;
                    });
                  },
                  selectedColor: AppTheme.primaryRed.withAlpha(51),
                  labelStyle: TextStyle(
                    color: isSelected ? AppTheme.primaryRed : null,
                    fontWeight: isSelected ? FontWeight.bold : null,
                  ),
                );
              }).toList(),
            ),
            const SizedBox(height: 20),

            // Subcategory Selection
            if (_currentSubcategories.isNotEmpty) ...[
              Text(
                'Pilih Subtopik',
                style: Theme.of(context).textTheme.titleSmall?.copyWith(
                      fontWeight: FontWeight.bold,
                    ),
              ),
              const SizedBox(height: 8),
              Wrap(
                spacing: 8,
                runSpacing: 8,
                children: [
                  // All option
                  ChoiceChip(
                    label: const Text('Semua'),
                    selected: _selectedSubcategory == null,
                    onSelected: (_) {
                      setState(() => _selectedSubcategory = null);
                    },
                    selectedColor: AppTheme.primaryRed.withAlpha(51),
                  ),
                  ..._currentSubcategories.map((sub) {
                    final isSelected = _selectedSubcategory == sub;
                    return ChoiceChip(
                      label: Text(sub),
                      selected: isSelected,
                      onSelected: (selected) {
                        setState(() =>
                            _selectedSubcategory = selected ? sub : null);
                      },
                      selectedColor: AppTheme.primaryRed.withAlpha(51),
                      labelStyle: TextStyle(
                        color:
                            isSelected ? AppTheme.primaryRed : null,
                        fontWeight: isSelected ? FontWeight.bold : null,
                        fontSize: 12,
                      ),
                    );
                  }),
                ],
              ),
              const SizedBox(height: 32),
            ],

            // Start Button
            SizedBox(
              width: double.infinity,
              child: ElevatedButton.icon(
                onPressed: _isLoading ? null : _startPractice,
                style: ElevatedButton.styleFrom(
                  padding: const EdgeInsets.symmetric(vertical: 16),
                ),
                icon: _isLoading
                    ? const SizedBox(
                        width: 20,
                        height: 20,
                        child: CircularProgressIndicator(
                          strokeWidth: 2,
                          valueColor:
                              AlwaysStoppedAnimation<Color>(Colors.white),
                        ),
                      )
                    : const Icon(Icons.play_arrow),
                label: Text(
                    _isLoading ? 'Memuat...' : 'Mulai Latihan'),
              ),
            ),
          ],
        ),
      ),
        ),
      ),
    );
  }

  Future<void> _startPractice() async {
    if (_selectedCategory == null) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Pilih kategori terlebih dahulu'),
          backgroundColor: AppTheme.warningOrange,
        ),
      );
      return;
    }

    setState(() => _isLoading = true);

    try {
      final repo = ref.read(questionRepositoryProvider);
      final questions = await repo.getPracticeQuestions(
        category: _selectedCategory!,
        subcategory: _selectedSubcategory,
      );

      if (!mounted) return;

      if (questions.isEmpty) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(
            content: Text('Tidak ada soal untuk subtopik ini'),
            backgroundColor: AppTheme.errorRed,
          ),
        );
        setState(() => _isLoading = false);
        return;
      }

      ref.read(tryoutProvider.notifier).startPracticeWithQuestions(questions);
      setState(() => _isLoading = false);

      if (mounted) {
        context.push('/tryout/PRACTICE');
      }
    } catch (e) {
      setState(() => _isLoading = false);
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('Gagal memuat soal: $e'),
            backgroundColor: AppTheme.errorRed,
          ),
        );
      }
    }
  }
}