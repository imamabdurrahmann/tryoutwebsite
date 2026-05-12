# TryOutCPNS - Specification Document

## 1. Project Overview
- **Project Name**: TryOutCPNS
- **Project Type**: Flutter Mobile Application (Android/iOS)
- **Core Functionality**: Aplikasi latihan soal Seleksi Kompetensi Dasar (SKD) untuk persiapan ujian_cpns dengan fitur try out lengkap, latihan per subtopik, dan statistik progres.

## 2. Technology Stack & Choices
- **Framework**: Flutter 3.16+
- **Language**: Dart 3.3+
- **State Management**: Riverpod 2.5+ with StateNotifier pattern
- **Navigation**: GoRouter 13+
- **Local Database**: Isar 3.1+ (offline-first, persistent storage)
- **HTTP Client**: Dio 5.4+ (for optional remote question updates)
- **Charts**: fl_chart 0.67+
- **Notifications**: flutter_local_notifications 17+
- **Architecture Pattern**: Clean Architecture (data/domain/presentation layers)

## 3. Feature List

### Core Features
1. **Home Screen** - Dashboard dengan paket try out dan statistik ringkas
2. **Try Out Screen** - Timer countdown, navigasi soal, flag/tandai, auto-submit
3. **Result Screen** - Skor total & per kategori, status LULUS/TIDAK LULUS, passing grade
4. **Review Screen** - Pembahasan soal dengan filter (benar/salah/tidak dijawab)
5. **History Screen** - Riwayat sesi, line chart progres, radar chart akurasi
6. **Practice Screen** - Latihan per subtopik tanpa timer, instant feedback
7. **Profile Screen** - Dark mode toggle, pengaturan reminder, info app

### Data Features
8. **Offline-First** - Load dari assets JSON, cache di Isar, cek update remote
9. **Persistent Storage** - Riwayat hasil di Isar, pengaturan di SharedPreferences
10. **Scoring System** - TWK/TIU: +5 benar, 0 salah; TKP: A=5, B=4, C=3, D=2, E=1

## 4. UI/UX Design Direction
- **Visual Style**: Material Design 3
- **Color Scheme**: Primary #C0392B (merah), Secondary #2980B9 (biru), full dark mode support
- **Layout**: Tab-based navigation via AppBar, bottom sheet question navigator
- **Animations**: Smooth page transitions, selected answer animations, progress indicators
- **Typography**: Default Material 3, responsive to dark mode
