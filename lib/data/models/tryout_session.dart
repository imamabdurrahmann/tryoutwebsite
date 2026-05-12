import 'dart:convert';
import 'package:hive/hive.dart';

part 'tryout_session.g.dart';

@HiveType(typeId: 1)
class TryoutSession extends HiveObject {
  @HiveField(0)
  late String sessionId;

  @HiveField(1)
  late String packageType;

  @HiveField(2)
  late DateTime startTime;

  @HiveField(3)
  DateTime? endTime;

  @HiveField(4)
  late int durationSeconds;

  @HiveField(5)
  late String answersJson;

  @HiveField(6)
  late List<String> flaggedQuestions;

  @HiveField(7)
  late int totalScore;

  @HiveField(8)
  late int twkScore;

  @HiveField(9)
  late int tiuScore;

  @HiveField(10)
  late int tkpScore;

  @HiveField(11)
  late bool twkPassed;

  @HiveField(12)
  late bool tiuPassed;

  @HiveField(13)
  late bool tkpPassed;

  @HiveField(14)
  late bool overallPassed;

  @HiveField(15)
  late int twkCorrect;

  @HiveField(16)
  late int tiuCorrect;

  @HiveField(17)
  late int tkpAnswered;

  @HiveField(18)
  late int twkWrong;

  @HiveField(19)
  late int tiuWrong;

  @HiveField(20)
  late int twkUnanswered;

  @HiveField(21)
  late int tiuUnanswered;

  @HiveField(22)
  late int tkpUnanswered;

  @HiveField(23)
  late int twkQuestionCount;

  @HiveField(24)
  late int tiuQuestionCount;

  @HiveField(25)
  late int tkpQuestionCount;

  TryoutSession();

  TryoutSession.create({
    required this.sessionId,
    required this.packageType,
    required this.startTime,
    this.endTime,
    required this.durationSeconds,
    required this.answersJson,
    required this.flaggedQuestions,
    required this.totalScore,
    required this.twkScore,
    required this.tiuScore,
    required this.tkpScore,
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

  /// Answers disimpan sebagai label (A/B/C/D/E) — konversi ke teks saat perlu.
  Map<String, String> get answers {
    if (answersJson.isEmpty) return {};
    try {
      final decoded = jsonDecode(answersJson);
      return Map<String, String>.from(decoded);
    } catch (_) {
      return {};
    }
  }

  set answers(Map<String, String> value) {
    answersJson = jsonEncode(value);
  }

  /// Label-to-text lookup (dipanggil dari ReviewScreen saat render options).
  /// returns Map<questionId, optionText>
  Map<String, String> get answerLabels {
    return answers; // Labels (A-E) — used by rendering code
  }

  int get durationMinutes => durationSeconds ~/ 60;

  bool get isCompleted => endTime != null;

  String get packageLabel {
    // Paket 2 detection
    final isP2 = packageType.endsWith('_2');
    final p2tag = isP2 ? ' Paket 2' : ' Paket 1';

    switch (packageType) {
      case 'FULL':
      case 'FULL_2':
        return 'Try Out Lengkap$p2tag';
      case 'TWK_ONLY':
      case 'TWK_ONLY_2':
        return 'Latihan TWK$p2tag';
      case 'TIU_ONLY':
      case 'TIU_ONLY_2':
        return 'Latihan TIU$p2tag';
      case 'TKP_ONLY':
      case 'TKP_ONLY_2':
        return 'Latihan TKP$p2tag';
      case 'PRACTICE':
        return 'Latihan Subtopik';
      default:
        return 'Try Out';
    }
  }

  bool get isFull => packageType == 'FULL' || packageType == 'FULL_2';
  bool get isTwkOnly => packageType == 'TWK_ONLY' || packageType == 'TWK_ONLY_2';
  bool get isTiuOnly => packageType == 'TIU_ONLY' || packageType == 'TIU_ONLY_2';
  bool get isTkpOnly => packageType == 'TKP_ONLY' || packageType == 'TKP_ONLY_2';

  int get maxTotalScore {
    if (isFull) return 550;
    if (isTwkOnly) return 150;
    if (isTiuOnly) return 175;
    if (isTkpOnly) return 225;
    return 550;
  }

  String get passingGradeInfo {
    if (isFull) return 'TWK≥65, TIU≥80, TKP≥166';
    if (isTwkOnly) return 'Passing Grade: 65';
    if (isTiuOnly) return 'Passing Grade: 80';
    if (isTkpOnly) return 'Passing Grade: 166';
    return '';
  }
}