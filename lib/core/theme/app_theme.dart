import 'package:flutter/material.dart';

class AppTheme {
  // Brand Colors (Merah-Putih)
  static const Color primaryRed = Color(0xFFC0392B);
  static const Color primaryRedDark = Color(0xFF922B21);
  static const Color primaryRedLight = Color(0xFFE74C3C);
  static const Color secondaryBlue = Color(0xFF2980B9);
  static const Color secondaryBlueDark = Color(0xFF1A5276);
  static const Color white = Color(0xFFFFFFFF);

  // Status Colors
  static const Color successGreen = Color(0xFF27AE60);
  static const Color errorRed = Color(0xFFE74C3C);
  static const Color warningOrange = Color(0xFFF39C12);
  static const Color infoBlue = Color(0xFF2980B9);

  // Question Status Colors
  static const Color answeredColor = Color(0xFF27AE60);
  static const Color flaggedColor = Color(0xFFF39C12);
  static const Color unansweredColor = Color(0xFF95A5A6);
  static const Color currentColor = Color(0xFF2980B9);

  // BKN CAT System Colors (4-color system)
  static const Color catUnvisited = Color(0xFF9E9E9E); // Abu-abu: belum dikunjungi
  static const Color catVisitedEmpty = Color(0xFFE53935); // Merah: dikunjungi tapi kosong
  static const Color catAnswered = Color(0xFF43A047); // Hijau: sudah dijawab
  static const Color catFlagged = Color(0xFFFFB300); // Kuning: ragu-ragu

  static ThemeData lightTheme() {
    final colorScheme = ColorScheme.fromSeed(
      seedColor: primaryRed,
      primary: primaryRed,
      secondary: secondaryBlue,
      brightness: Brightness.light,
      surface: const Color(0xFFFAFAFA),
      error: errorRed,
    );

    return ThemeData(
      useMaterial3: true,
      colorScheme: colorScheme,
      scaffoldBackgroundColor: const Color(0xFFF5F5F5),
      appBarTheme: AppBarTheme(
        backgroundColor: primaryRed,
        foregroundColor: white,
        elevation: 0,
        centerTitle: true,
        titleTextStyle: const TextStyle(
          color: white,
          fontSize: 18,
          fontWeight: FontWeight.w600,
        ),
      ),
      cardTheme: CardTheme(
        elevation: 2,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
        color: Colors.white,
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: primaryRed,
          foregroundColor: white,
          elevation: 2,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(10),
          ),
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
        ),
      ),
      outlinedButtonTheme: OutlinedButtonThemeData(
        style: OutlinedButton.styleFrom(
          foregroundColor: primaryRed,
          side: const BorderSide(color: primaryRed),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(10),
          ),
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
        ),
      ),
      inputDecorationTheme: InputDecorationTheme(
        border: OutlineInputBorder(borderRadius: BorderRadius.circular(10)),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(10),
          borderSide: const BorderSide(color: primaryRed, width: 2),
        ),
      ),
      chipTheme: ChipThemeData(
        backgroundColor: primaryRed.withAlpha(26),
        labelStyle: const TextStyle(color: primaryRed),
        selectedColor: primaryRed,
      ),
      floatingActionButtonTheme: const FloatingActionButtonThemeData(
        backgroundColor: primaryRed,
        foregroundColor: white,
      ),
      bottomNavigationBarTheme: const BottomNavigationBarThemeData(
        selectedItemColor: primaryRed,
        unselectedItemColor: Colors.grey,
      ),
      dividerTheme: const DividerThemeData(thickness: 1, color: Color(0xFFEEEEEE)),
      progressIndicatorTheme: const ProgressIndicatorThemeData(color: primaryRed),
    );
  }

  static ThemeData darkTheme() {
    final colorScheme = ColorScheme.fromSeed(
      seedColor: primaryRed,
      primary: primaryRedLight,
      secondary: secondaryBlue,
      brightness: Brightness.dark,
      surface: const Color(0xFF1E1E1E),
      error: errorRed,
    );

    return ThemeData(
      useMaterial3: true,
      colorScheme: colorScheme,
      scaffoldBackgroundColor: const Color(0xFF121212),
      appBarTheme: AppBarTheme(
        backgroundColor: const Color(0xFF1E1E1E),
        foregroundColor: white,
        elevation: 0,
        centerTitle: true,
        titleTextStyle: const TextStyle(
          color: white,
          fontSize: 18,
          fontWeight: FontWeight.w600,
        ),
      ),
      cardTheme: CardTheme(
        elevation: 2,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
        color: const Color(0xFF2C2C2C),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: primaryRed,
          foregroundColor: white,
          elevation: 2,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(10),
          ),
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
        ),
      ),
      outlinedButtonTheme: OutlinedButtonThemeData(
        style: OutlinedButton.styleFrom(
          foregroundColor: primaryRedLight,
          side: const BorderSide(color: primaryRedLight),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(10),
          ),
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
        ),
      ),
      floatingActionButtonTheme: const FloatingActionButtonThemeData(
        backgroundColor: primaryRed,
        foregroundColor: white,
      ),
      bottomNavigationBarTheme: const BottomNavigationBarThemeData(
        backgroundColor: Color(0xFF1E1E1E),
        selectedItemColor: primaryRedLight,
        unselectedItemColor: Colors.grey,
      ),
      dividerTheme: const DividerThemeData(thickness: 1, color: Color(0xFF3A3A3A)),
      progressIndicatorTheme: const ProgressIndicatorThemeData(color: primaryRedLight),
    );
  }
}
