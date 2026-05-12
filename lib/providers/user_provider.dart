import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../data/models/user_settings.dart';
import '../data/repositories/user_repository.dart';
import '../core/utils/notification_service.dart';

final userRepositoryProvider = Provider((ref) => UserRepository());
final notificationServiceProvider = Provider((ref) => NotificationService());

class UserSettingsNotifier extends StateNotifier<UserSettings> {
  final UserRepository _repository;
  // ignore: unused_field
  final NotificationService _notificationService;

  UserSettingsNotifier(this._repository, this._notificationService)
      : super(UserSettings()) {
    _load();
  }

  void _load() {
    state = _repository.getUserSettings();
  }

  Future<void> setDarkMode(bool enabled) async {
    await _repository.setDarkMode(enabled);
    state = state.copyWith(darkMode: enabled);
  }

  Future<void> setDailyReminder({
    required bool enabled,
    required int hour,
    required int minute,
  }) async {
    await _repository.setDailyReminder(
      enabled: enabled,
      hour: hour,
      minute: minute,
    );
    state = state.copyWith(
      dailyReminderEnabled: enabled,
      reminderHour: hour,
      reminderMinute: minute,
    );
  }
}

final userSettingsProvider = StateNotifierProvider<UserSettingsNotifier, UserSettings>((ref) {
  final repository = ref.watch(userRepositoryProvider);
  final notificationService = ref.watch(notificationServiceProvider);
  return UserSettingsNotifier(repository, notificationService);
});

final darkModeProvider = Provider<bool>((ref) {
  return ref.watch(userSettingsProvider).darkMode;
});

final statsProvider = FutureProvider<Map<String, dynamic>>((ref) async {
  final repository = ref.watch(userRepositoryProvider);
  final totalSessions = repository.getTotalSessions();
  final streak = repository.getStreak();

  return {
    'totalSessions': totalSessions,
    'streak': streak,
  };
});

// Provider to trigger refresh rebuilds across the app
final refreshTriggerProvider = StateProvider<int>((ref) => 0);
