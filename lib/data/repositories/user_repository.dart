import 'package:shared_preferences/shared_preferences.dart';
import '../../core/constants/app_constants.dart';
import '../../core/utils/notification_service.dart';
import '../models/user_settings.dart';
import '../sources/hive_source.dart';

class UserRepository {
  final HiveSource _hiveSource = HiveSource();
  final NotificationService _notificationService = NotificationService();

  UserSettings getUserSettings() {
    return _hiveSource.getUserSettings();
  }

  Future<void> saveUserSettings(UserSettings settings) async {
    await _hiveSource.saveUserSettings(settings);
  }

  Future<void> setDarkMode(bool enabled) async {
    final settings = getUserSettings();
    settings.darkMode = enabled;
    await saveUserSettings(settings);

    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(AppConstants.prefDarkMode, enabled);
  }

  Future<void> setDailyReminder({
    required bool enabled,
    required int hour,
    required int minute,
  }) async {
    final settings = getUserSettings();
    settings.dailyReminderEnabled = enabled;
    settings.reminderHour = hour;
    settings.reminderMinute = minute;
    await saveUserSettings(settings);

    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(AppConstants.prefDailyReminder, enabled);
    await prefs.setInt(AppConstants.prefReminderHour, hour);
    await prefs.setInt(AppConstants.prefReminderMinute, minute);

    if (enabled) {
      await _notificationService.scheduleDailyReminder(
        hour: hour,
        minute: minute,
      );
    } else {
      await _notificationService.cancelDailyReminder();
    }
  }

  Future<void> incrementSessionCount() async {
    final settings = getUserSettings();
    settings.totalSessions++;

    final now = DateTime.now();
    final today = '${now.year}-${now.month.toString().padLeft(2, '0')}-${now.day.toString().padLeft(2, '0')}';

    if (settings.lastSessionDate == today) {
      // Same day, no streak update needed
    } else {
      final yesterday = now.subtract(const Duration(days: 1));
      final yesterdayStr = '${yesterday.year}-${yesterday.month.toString().padLeft(2, '0')}-${yesterday.day.toString().padLeft(2, '0')}';

      if (settings.lastSessionDate == yesterdayStr) {
        settings.streak++;
      } else {
        settings.streak = 1;
      }
    }

    settings.lastSessionDate = today;
    await saveUserSettings(settings);
  }

  int getStreak() {
    return getUserSettings().streak;
  }

  int getTotalSessions() {
    return getUserSettings().totalSessions;
  }
}
