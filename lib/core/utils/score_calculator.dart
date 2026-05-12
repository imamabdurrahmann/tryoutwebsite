import '../../core/constants/app_constants.dart';
import '../../data/models/question.dart';

class ScoreResult {
  final int twkRaw;       // Skor mentah TWK (0–150): 30 soal × 5
  final int tiuRaw;       // Skor mentah TIU (0–175): 35 soal × 5
  final int tkpScore;     // Skor TKP (0–225): 45 soal × A5/B4/C3/D2/E1
  final int twkScaled;    // Skor TWK dikonversi ke skala 100
  final int tiuScaled;    // Skor TIU dikonversi ke skala 100
  final bool twkPassed;
  final bool tiuPassed;
  final bool tkpPassed;
  final bool overallPassed;
  final int twkCorrect;
  final int tiuCorrect;
  final int tkpAnswered;
  final int twkWrong;
  final int tiuWrong;
  final int twkUnanswered;
  final int tiuUnanswered;
  final int tkpUnanswered;
  final int twkQuestionCount;
  final int tiuQuestionCount;
  final int tkpQuestionCount;

  const ScoreResult({
    required this.twkRaw,
    required this.tiuRaw,
    required this.tkpScore,
    required this.twkScaled,
    required this.tiuScaled,
    required this.twkPassed,
    required this.tiuPassed,
    required this.tkpPassed,
    required this.overallPassed,
    required this.twkCorrect,
    required this.tiuCorrect,
    required this.tkpAnswered,
    required this.twkWrong,
    required this.tiuWrong,
    required this.twkUnanswered,
    required this.tiuUnanswered,
    required this.tkpUnanswered,
    required this.twkQuestionCount,
    required this.tiuQuestionCount,
    required this.tkpQuestionCount,
  });

  int get totalScore => twkScaled + tiuScaled + tkpScore;
}

class ScoreCalculator {
  /// Hitung skor dari daftar soal dan jawaban pengguna.
  /// [answers] = Map<questionId, jawabanPengguna>
  /// [packageType] = tipe paket ('FULL', 'TWK_ONLY', 'TIU_ONLY', 'TKP_ONLY', dll)
  /// Jika null, default ke logika FULL (semua kategori harus lulus).
  static ScoreResult calculate(
    List<Question> questions,
    Map<String, String> answers, [
    String? packageType,
  ]) {
    int twkRaw = 0;
    int tiuRaw = 0;
    int tkpScore = 0;

    int twkCorrect = 0;
    int tiuCorrect = 0;
    int tkpAnswered = 0;
    int twkWrong = 0;
    int tiuWrong = 0;
    int twkUnanswered = 0;
    int tiuUnanswered = 0;
    int tkpUnanswered = 0;

    int twkQuestionCount = 0;
    int tiuQuestionCount = 0;
    int tkpQuestionCount = 0;

    for (final q in questions) {
      // Count questions per category
      switch (q.category) {
        case 'TWK':
          twkQuestionCount++;
          break;
        case 'TIU':
          tiuQuestionCount++;
          break;
        case 'TKP':
          tkpQuestionCount++;
          break;
      }

      final userAnswer = answers[q.questionId];

      switch (q.category) {
        case 'TWK':
          if (userAnswer == null || userAnswer.isEmpty) {
            twkUnanswered++;
          } else if (userAnswer == q.answer) {
            twkRaw += AppConstants.twkCorrectScore;
            twkCorrect++;
          } else {
            twkWrong++;
          }
          break;

        case 'TIU':
          if (userAnswer == null || userAnswer.isEmpty) {
            tiuUnanswered++;
          } else if (userAnswer == q.answer) {
            tiuRaw += AppConstants.tiuCorrectScore;
            tiuCorrect++;
          } else {
            tiuWrong++;
          }
          break;

        case 'TKP':
          if (userAnswer == null || userAnswer.isEmpty) {
            tkpUnanswered++;
          } else {
            final score = _getTkpScore(userAnswer, q.answer);
            tkpScore += score;
            tkpAnswered++;
          }
          break;
      }
    }

    // Konversi TWK & TIU ke skala 100
    // TWK: raw/150 * 100 (30 soal × 5 = 150), TIU: raw/175 * 100 (35 soal × 5 = 175)
    final twkScaled = _scaleScore(twkRaw, AppConstants.twkMaxScore, 100);
    final tiuScaled = _scaleScore(tiuRaw, AppConstants.tiuMaxScore, 100);

    final twkPassed = twkScaled >= AppConstants.twkPassingGrade;
    final tiuPassed = tiuScaled >= AppConstants.tiuPassingGrade;
    final tkpPassed = tkpScore >= AppConstants.tkpPassingGrade;

    // ✅ DATA DRIVEN: overallPassed sesuai jenis paket
    bool overallPassed;
    if (packageType == 'TWK_ONLY' || packageType == 'TWK_ONLY_2') {
      overallPassed = twkPassed; // Hanya TWK yang dihitung
    } else if (packageType == 'TIU_ONLY' || packageType == 'TIU_ONLY_2') {
      overallPassed = tiuPassed; // Hanya TIU yang dihitung
    } else if (packageType == 'TKP_ONLY' || packageType == 'TKP_ONLY_2') {
      overallPassed = tkpPassed; // Hanya TKP yang dihitung
    } else {
      // FULL: semua harus lulus
      overallPassed = twkPassed && tiuPassed && tkpPassed;
    }

    return ScoreResult(
      twkRaw: twkRaw,
      tiuRaw: tiuRaw,
      tkpScore: tkpScore,
      twkScaled: twkScaled,
      tiuScaled: tiuScaled,
      twkPassed: twkPassed,
      tiuPassed: tiuPassed,
      tkpPassed: tkpPassed,
      overallPassed: overallPassed,
      twkCorrect: twkCorrect,
      tiuCorrect: tiuCorrect,
      tkpAnswered: tkpAnswered,
      twkWrong: twkWrong,
      tiuWrong: tiuWrong,
      twkUnanswered: twkUnanswered,
      tiuUnanswered: tiuUnanswered,
      tkpUnanswered: tkpUnanswered,
      twkQuestionCount: twkQuestionCount,
      tiuQuestionCount: tiuQuestionCount,
      tkpQuestionCount: tkpQuestionCount,
    );
  }

  /// Untuk TKP: opsi A(benar utama)=5, B=4, C=3, D=2, E=1
  /// Sistem TKP tidak ada jawaban mutlak salah, semua dapat skor
  static int _getTkpScore(String userAnswer, String correctAnswer) {
    // Mapping posisi jawaban ke skor (A=5 paling tepat, E=1 paling kurang tepat)
    const scoreMap = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1};
    return scoreMap[userAnswer] ?? 1;
  }

  static int _scaleScore(int raw, int maxRaw, int maxScale) {
    if (maxRaw == 0) return 0;
    return ((raw / maxRaw) * maxScale).round();
  }

  /// Hitung akurasi per subcategory
  static Map<String, double> calculateSubcategoryAccuracy(
    List<Question> questions,
    Map<String, String> answers,
  ) {
    final Map<String, int> correct = {};
    final Map<String, int> total = {};

    for (final q in questions) {
      final sub = q.subcategory;
      total[sub] = (total[sub] ?? 0) + 1;

      final userAnswer = answers[q.questionId];
      if (q.category != 'TKP' && userAnswer == q.answer) {
        correct[sub] = (correct[sub] ?? 0) + 1;
      } else if (q.category == 'TKP' && userAnswer != null) {
        // TKP: hitung sebagai "benar" jika pilih A (skor tertinggi)
        if (userAnswer == 'A') {
          correct[sub] = (correct[sub] ?? 0) + 1;
        }
      }
    }

    final Map<String, double> accuracy = {};
    for (final sub in total.keys) {
      accuracy[sub] = (correct[sub] ?? 0) / total[sub]!;
    }
    return accuracy;
  }
}
