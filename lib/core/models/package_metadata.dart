/// Metadata model untuk setiap paket tryout.
/// Digunakan secara sentral untuk menghindari hardcode di seluruh codebase.

class PackageMetadata {
  final String packageId;
  final String title;
  final String subtitle;
  final int totalQuestions;
  final int durationMinutes;

  const PackageMetadata({
    required this.packageId,
    required this.title,
    required this.subtitle,
    required this.totalQuestions,
    required this.durationMinutes,
  });

  /// Format ringkas: "[title] ([subtitle])\n[total] Soal • [duration] Menit"
  String get formattedSummary =>
      '$title ($subtitle)\n$totalQuestions Soal • $durationMinutes Menit';

  /// Helper: apakah ini paket lengkap (TOL)
  bool get isFull => packageId == 'FULL' || packageId == 'FULL_2';

  /// Helper: apakah ini paket latihan tunggal
  bool get isSingleCategory =>
      packageId.startsWith('TWK_ONLY') ||
      packageId.startsWith('TIU_ONLY') ||
      packageId.startsWith('TKP_ONLY');

  /// Helper: kategori TWK
  bool get isTwk => packageId.startsWith('TWK_ONLY');

  /// Helper: kategori TIU
  bool get isTiu => packageId.startsWith('TIU_ONLY');

  /// Helper: kategori TKP
  bool get isTkp => packageId.startsWith('TKP_ONLY');
}

/// Repository sentral untuk metadata paket.
/// Single source of truth — satu tempat untuk definisi semua paket.
///
/// Contoh usage:
///   final meta = PackageMetadataRepository.get('FULL_2');
///   print(meta.formattedSummary); // Try Out Lengkap (Paket 2)\n110 Soal • 100 Menit
class PackageMetadataRepository {
  PackageMetadataRepository._();

  static const _registry = <String, PackageMetadata>{
    // ===== PAKET 1 =====
    'FULL': PackageMetadata(
      packageId: 'FULL',
      title: 'Try Out Lengkap',
      subtitle: 'Paket 1',
      totalQuestions: 110,
      durationMinutes: 100,
    ),
    'TWK_ONLY': PackageMetadata(
      packageId: 'TWK_ONLY',
      title: 'Latihan TWK',
      subtitle: 'Paket 1',
      totalQuestions: 30,
      durationMinutes: 30,
    ),
    'TIU_ONLY': PackageMetadata(
      packageId: 'TIU_ONLY',
      title: 'Latihan TIU',
      subtitle: 'Paket 1',
      totalQuestions: 35,
      durationMinutes: 35,
    ),
    'TKP_ONLY': PackageMetadata(
      packageId: 'TKP_ONLY',
      title: 'Latihan TKP',
      subtitle: 'Paket 1',
      totalQuestions: 45,
      durationMinutes: 45,
    ),
    // ===== PAKET 2 =====
    'FULL_2': PackageMetadata(
      packageId: 'FULL_2',
      title: 'Try Out Lengkap',
      subtitle: 'Paket 2',
      totalQuestions: 110,
      durationMinutes: 100,
    ),
    'TWK_ONLY_2': PackageMetadata(
      packageId: 'TWK_ONLY_2',
      title: 'Latihan TWK',
      subtitle: 'Paket 2',
      totalQuestions: 30,
      durationMinutes: 30,
    ),
    'TIU_ONLY_2': PackageMetadata(
      packageId: 'TIU_ONLY_2',
      title: 'Latihan TIU',
      subtitle: 'Paket 2',
      totalQuestions: 35,
      durationMinutes: 35,
    ),
    'TKP_ONLY_2': PackageMetadata(
      packageId: 'TKP_ONLY_2',
      title: 'Latihan TKP',
      subtitle: 'Paket 2',
      totalQuestions: 45,
      durationMinutes: 45,
    ),
    // ===== PAKET 3 =====
    'FULL_3': PackageMetadata(
      packageId: 'FULL_3',
      title: 'Try Out Lengkap',
      subtitle: 'Paket 3',
      totalQuestions: 110,
      durationMinutes: 100,
    ),
    'TWK_ONLY_3': PackageMetadata(
      packageId: 'TWK_ONLY_3',
      title: 'Latihan TWK',
      subtitle: 'Paket 3',
      totalQuestions: 30,
      durationMinutes: 30,
    ),
    'TIU_ONLY_3': PackageMetadata(
      packageId: 'TIU_ONLY_3',
      title: 'Latihan TIU',
      subtitle: 'Paket 3',
      totalQuestions: 35,
      durationMinutes: 35,
    ),
    'TKP_ONLY_3': PackageMetadata(
      packageId: 'TKP_ONLY_3',
      title: 'Latihan TKP',
      subtitle: 'Paket 3',
      totalQuestions: 45,
      durationMinutes: 45,
    ),
  };

  /// Ambil metadata berdasarkan packageId.
  /// Fallback ke Paket 1 jika tidak ditemukan (forward-compatible).
  static PackageMetadata get(String packageId) {
    return _registry[packageId] ?? _registry['FULL']!;
  }

  /// Ambil semua metadata yang terdaftar.
  static List<PackageMetadata> get all => _registry.values.toList();

  /// Ambil metadata berdasarkan kategori dasar (tanpa suffix paket).
  /// Contoh: getByBase('FULL') → [FULL Paket 1, FULL Paket 2]
  static List<PackageMetadata> getByBase(String baseId) {
    return _registry.values
        .where((m) => m.packageId == baseId || m.packageId.startsWith('${baseId}_'))
        .toList();
  }
}
