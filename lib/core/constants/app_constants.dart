class AppConstants {
  // App Info
  static const String appName = 'JagoanCPNS';
  static const String appVersion = '1.0.0';

  // Passing Grade 2024 (SKDCPNS)
  static const int twkPassingGrade = 65;
  static const int tiuPassingGrade = 80;
  static const int tkpPassingGrade = 166;

  // Jumlah Soal (standar SKD 2024)
  static const int twkQuestionCount = 30;
  static const int tiuQuestionCount = 35;
  static const int tkpQuestionCount = 45;
  static const int totalQuestionCount = 110; // 30+35+45

  // Skor: TWK & TIU = Benar 5, Salah/Kosong 0. TKP = A5, B4, C3, D2, E1.
  static const int twkCorrectScore = 5;
  static const int tiuCorrectScore = 5;
  static const int twkMaxScore = twkQuestionCount * twkCorrectScore; // 150
  static const int tiuMaxScore = tiuQuestionCount * tiuCorrectScore; // 175
  static const int tkpMaxScore = tkpQuestionCount * 5; // 225

  // Durasi SKD 2024 (detik)
  static const int fullTryoutDuration = 100 * 60;  // 110 soal, 100 menit
  static const int twkOnlyDuration = 30 * 60;      // 30 soal, 30 menit
  static const int tiuOnlyDuration = 35 * 60;       // 35 soal, 35 menit
  static const int tkpOnlyDuration = 45 * 60;     // 45 soal, 45 menit

  // Package Types
  static const String packageFull = 'FULL';
  static const String packageTwk = 'TWK_ONLY';
  static const String packageTiu = 'TIU_ONLY';
  static const String packageTkp = 'TKP_ONLY';
  static const String packagePractice = 'PRACTICE';

  // Categories
  static const String categoryTwk = 'TWK';
  static const String categoryTiu = 'TIU';
  static const String categoryTkp = 'TKP';

  // TWK Subcategories — SESUAI dengan JSON Paket 1 & 2
  static const List<String> twkSubcategories = [
    'Nasionalisme',
    'Integritas',
    'Bela Negara',
    'Pilar Negara',
    'Bahasa Indonesia',
  ];

  // TIU Subcategories — SESUAI dengan JSON Paket 1 & 2
  static const List<String> tiuSubcategories = [
    'Analogi',
    'Silogisme',
    'Analitis',
    'Deret',
    'Aritmetika',
    'Cerita Matematika',
    'Figural',
  ];

  // TKP Subcategories — SESUAI dengan JSON Paket 1 & 2
  static const List<String> tkpSubcategories = [
    'Pelayanan Publik',
    'Jejaring Kerja',
    'Sosial Budaya',
    'TIK',
    'Profesionalisme',
    'Integritas Diri',
  ];

  // Difficulty
  static const String difficultyEasy = 'easy';
  static const String difficultyMedium = 'medium';
  static const String difficultyHard = 'hard';

  // Practice question counts
  static const List<int> practiceQuestionCounts = [10, 20, 30];

  // Assets paths — Package 1 (default)
  static const String twkJsonPath = 'assets/questions/twk.json';
  static const String tiuJsonPath = 'assets/questions/tiu.json';
  static const String tkpJsonPath = 'assets/questions/tkp.json';

  // Assets paths — Package 2
  static const String twkJsonPath2 = 'assets/questions/twk_2.json';
  static const String tiuJsonPath2 = 'assets/questions/tiu_2.json';
  static const String tkpJsonPath2 = 'assets/questions/tkp_2.json';
  static const String fullJsonPath2 = 'assets/questions/full_2.json';

  // Assets paths — Package 3
  static const String twkJsonPath3 = 'assets/questions/twk_3.json';
  static const String tiuJsonPath3 = 'assets/questions/tiu_3.json';
  static const String tkpJsonPath3 = 'assets/questions/tkp_3.json';

  // API
  static const String apiBaseUrl = 'https://api.tryoutcpns.id';
  static const String apiQuestionsVersion = '/api/questions/version';
  static const String apiQuestions = '/api/questions';

  // Notification
  static const int dailyReminderNotificationId = 1001;
  static const String dailyReminderChannelId = 'daily_reminder';
  static const String dailyReminderChannelName = 'Pengingat Belajar Harian';

  // Shared Preferences Keys
  static const String prefDarkMode = 'dark_mode';
  static const String prefDailyReminder = 'daily_reminder_enabled';
  static const String prefReminderHour = 'reminder_hour';
  static const String prefReminderMinute = 'reminder_minute';
  static const String prefTotalSessions = 'total_sessions';
  static const String prefStreak = 'streak';
  static const String prefLastSessionDate = 'last_session_date';
  static const String prefQuestionsVersion = 'questions_version';

  /// Extract package number ('1', '2', '3') from packageType string.
  /// Examples:
  ///   'FULL' -> '1'
  ///   'FULL_2' -> '2'
  ///   'TWK_ONLY_3' -> '3'
  static String extractPackageNumber(String packageType) {
    if (packageType.endsWith('_3')) return '3';
    if (packageType.endsWith('_2')) return '2';
    return '1';
  }
}