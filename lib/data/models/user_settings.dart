import 'package:hive/hive.dart';

part 'user_settings.g.dart';

@HiveType(typeId: 2)
class UserSettings extends HiveObject {
  @HiveField(0)
  late bool dailyReminderEnabled;

  @HiveField(1)
  late int reminderHour;

  @HiveField(2)
  late int reminderMinute;

  @HiveField(3)
  late bool darkMode;

  @HiveField(4)
  late int totalSessions;

  @HiveField(5)
  late int streak;

  @HiveField(6)
  late String lastSessionDate;

  UserSettings() {
    dailyReminderEnabled = false;
    reminderHour = 8;
    reminderMinute = 0;
    darkMode = false;
    totalSessions = 0;
    streak = 0;
    lastSessionDate = '';
  }

  UserSettings.createDefault() {
    dailyReminderEnabled = false;
    reminderHour = 8;
    reminderMinute = 0;
    darkMode = false;
    totalSessions = 0;
    streak = 0;
    lastSessionDate = '';
  }

  UserSettings copyWith({
    bool? dailyReminderEnabled,
    int? reminderHour,
    int? reminderMinute,
    bool? darkMode,
    int? totalSessions,
    int? streak,
    String? lastSessionDate,
  }) {
    final copy = UserSettings();
    copy.dailyReminderEnabled = dailyReminderEnabled ?? this.dailyReminderEnabled;
    copy.reminderHour = reminderHour ?? this.reminderHour;
    copy.reminderMinute = reminderMinute ?? this.reminderMinute;
    copy.darkMode = darkMode ?? this.darkMode;
    copy.totalSessions = totalSessions ?? this.totalSessions;
    copy.streak = streak ?? this.streak;
    copy.lastSessionDate = lastSessionDate ?? this.lastSessionDate;
    return copy;
  }
}
