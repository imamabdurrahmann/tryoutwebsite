// ignore: unused_import
import 'package:intl/intl.dart' as intl;
import 'app_localizations.dart';

// ignore_for_file: type=lint

/// The translations for Indonesian (`id`).
class AppLocalizationsId extends AppLocalizations {
  AppLocalizationsId([String locale = 'id']) : super(locale);

  @override
  String get appTitle => 'TryOutCPNSbyIMAM';

  @override
  String get home => 'Beranda';

  @override
  String get tryout => 'Try Out';

  @override
  String get history => 'Riwayat';

  @override
  String get profile => 'Profil';

  @override
  String get practice => 'Latihan';

  @override
  String get start => 'Mulai';

  @override
  String get cancel => 'Batal';

  @override
  String get confirm => 'Konfirmasi';

  @override
  String get submit => 'Kirim';

  @override
  String get finish => 'Selesai';

  @override
  String get next => 'Selanjutnya';

  @override
  String get previous => 'Sebelumnya';

  @override
  String question(int number, int total) {
    return 'Soal $number dari $total';
  }

  @override
  String get totalScore => 'Total Skor';

  @override
  String get passingGrade => 'Passing Grade';

  @override
  String get lulus => 'LULUS';

  @override
  String get tidakLulus => 'TIDAK LULUS';

  @override
  String get correct => 'Benar';

  @override
  String get wrong => 'Salah';

  @override
  String get unanswered => 'Tidak Dijawab';

  @override
  String get explanation => 'Pembahasan';

  @override
  String get seeReview => 'Lihat Pembahasan';

  @override
  String get tryAgain => 'Coba Lagi';

  @override
  String get backToHome => 'Kembali';

  @override
  String get darkMode => 'Mode Gelap';

  @override
  String get dailyReminder => 'Pengingat Harian';

  @override
  String get reminderTime => 'Waktu Pengingat';

  @override
  String get settings => 'Pengaturan';

  @override
  String get about => 'Tentang';

  @override
  String get version => 'Versi';

  @override
  String get tryOutComplete => 'Try Out Lengkap';

  @override
  String get practiceTKW => 'Latihan TWK';

  @override
  String get practiceTIU => 'Latihan TIU';

  @override
  String get practiceTKP => 'Latihan TKP';

  @override
  String get practiceByTopic => 'Latihan Per Subtopik';
}
