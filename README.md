# TryOutCPNS

Aplikasi latihan soal Seleksi Kompetensi Dasar (SKD) untuk persiapan ujian_cpns.

## Getting Started

```bash
# Install dependencies
flutter pub get

# Generate Isar code (WAJIB)
dart run build_runner build --delete-conflicting-outputs

# Run the app
flutter run
```

## Project Structure (Clean Architecture)

```
lib/
├── core/           # Constants, theme, utilities, router
├── data/           # Models, repositories, data sources
├── features/       # Feature-based screens and widgets
└── providers/      # Riverpod providers
```

## Features

- Try Out Lengkap (115 soal, 90 menit)
- Latihan TWK / TIU / TKP per kategori
- Latihan per subtopik dengan instant feedback
- Review pembahasan soal
- Statistik dan grafik progres
- Dark mode
- Pengingat belajar harian
- Offline-first dengan Isar database

## Passing Grade SKB 2024

| Kategori | Passing Grade |
|----------|--------------|
| TWK      | ≥ 65         |
| TIU      | ≥ 80         |
| TKP      | ≥ 166        |
