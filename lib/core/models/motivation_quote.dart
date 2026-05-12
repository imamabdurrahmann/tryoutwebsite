import 'dart:math';

/// Model sederhana untuk pasangan headline + sub-headline motivasi.
class MotivationQuote {
  final String headline;
  final String subHeadline;

  const MotivationQuote({
    required this.headline,
    required this.subHeadline,
  });

  /// Daftar pasangan motivasi yang tersedia.
  static const List<MotivationQuote> _quotes = [
    MotivationQuote(
      headline: 'Satu Langkah Lebih Dekat',
      subHeadline: 'Percayalah pada prosesmu. Yuk, maksimalkan latihan hari ini!',
    ),
    MotivationQuote(
      headline: 'Usaha Tak Mengkhianati Hasil 🌟',
      subHeadline: 'Lakukan yang terbaik di sesi ini, biarkan Tuhan yang menuntun langkahmu.',
    ),
    MotivationQuote(
      headline: 'Niat Baik, Jalan Terbuka ✨',
      subHeadline: 'Doakan teman seperjuanganmu, niscaya kebaikan akan berbalik padamu.',
    ),
  ];

  /// Mengembalikan satu MotivationQuote secara acak.
  static MotivationQuote getRandom() {
    final random = Random();
    return _quotes[random.nextInt(_quotes.length)];
  }
}
