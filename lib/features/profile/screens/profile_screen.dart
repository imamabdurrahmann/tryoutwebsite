import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../../core/constants/app_constants.dart';
import '../../../core/theme/app_theme.dart';
import '../../../core/utils/app_utils.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../../../core/utils/notification_service.dart';
import '../../../providers/user_provider.dart';

class ProfileScreen extends ConsumerStatefulWidget {
  const ProfileScreen({super.key});

  @override
  ConsumerState<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends ConsumerState<ProfileScreen> {
  TimeOfDay _selectedTime = const TimeOfDay(hour: 8, minute: 0);
  double _fontScale = 1.0;

  @override
  void initState() {
    super.initState();
    _loadCurrentTime();
    _loadFontScale();
  }

  void _loadCurrentTime() {
    WidgetsBinding.instance.addPostFrameCallback((_) {
      final settings = ref.read(userSettingsProvider);
      setState(() {
        _selectedTime = TimeOfDay(
          hour: settings.reminderHour,
          minute: settings.reminderMinute,
        );
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    final settings = ref.watch(userSettingsProvider);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Pengaturan'),
      ),
      body: Center(
        child: ConstrainedBox(
          constraints: const BoxConstraints(maxWidth: 900),
          child: ListView(
        children: [
          // Appearance Section
          _buildSectionHeader('Tampilan'),
          SwitchListTile(
            title: const Text('Mode Gelap'),
            subtitle: const Text('Aktifkan tema gelap untuk mata lebih nyaman'),
            value: settings.darkMode,
            onChanged: (value) {
              ref.read(userSettingsProvider.notifier).setDarkMode(value);
            },
            secondary: const Icon(Icons.dark_mode),
          ),
          const Divider(),

          // Font Size Section
          _buildSectionHeader('Ukuran Teks'),
          ListTile(
            leading: const Icon(Icons.text_fields),
            title: const Text('Ukuran Font'),
            subtitle: Slider(
              value: _fontScale,
              min: 0.8,
              max: 1.4,
              divisions: 6,
              label: '${(_fontScale * 100).round()}%',
              onChanged: (value) {
                setState(() => _fontScale = value);
                _saveFontScale(value);
              },
            ),
            trailing: Text(
              '${(_fontScale * 100).round()}%',
              style: const TextStyle(fontWeight: FontWeight.bold),
            ),
          ),
          const Divider(),

          // Notifications Section
          _buildSectionHeader('Notifikasi'),
          SwitchListTile(
            title: const Text('Pengingat Belajar Harian'),
            subtitle: const Text('Aktifkan notifikasi pengingat setiap hari'),
            value: settings.dailyReminderEnabled,
            onChanged: (value) async {
              if (value) {
                // Request permission
                final notificationService = NotificationService();
                final granted = await notificationService.requestPermission();
                if (!granted) {
                  if (mounted) {
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(
                        content: Text('Izin notifikasi diperlukan'),
                        backgroundColor: AppTheme.warningOrange,
                      ),
                    );
                  }
                  return;
                }
              }

              ref.read(userSettingsProvider.notifier).setDailyReminder(
                    enabled: value,
                    hour: _selectedTime.hour,
                    minute: _selectedTime.minute,
                  );
            },
            secondary: const Icon(Icons.notifications),
          ),

          if (settings.dailyReminderEnabled) ...[
            ListTile(
              title: const Text('Waktu Pengingat'),
              subtitle: Text(_selectedTime.format(context)),
              leading: const Icon(Icons.access_time),
              trailing: const Icon(Icons.chevron_right),
              onTap: () => _selectTime(context),
            ),
          ],
          const Divider(),

          // Statistics Section
          _buildSectionHeader('Statistik'),
          ListTile(
            title: const Text('Total Sesi Try Out'),
            leading: const Icon(Icons.assignment),
            trailing: Text(
              '${settings.totalSessions}',
              style: const TextStyle(
                fontWeight: FontWeight.bold,
                color: AppTheme.primaryRed,
              ),
            ),
          ),
          ListTile(
            title: const Text('Hari Streak'),
            leading: const Icon(Icons.local_fire_department,
                color: AppTheme.warningOrange),
            trailing: Text(
              '${settings.streak}',
              style: const TextStyle(
                fontWeight: FontWeight.bold,
                color: AppTheme.warningOrange,
              ),
            ),
          ),
          const Divider(),

          // About Section
          _buildSectionHeader('Tentang'),
          ListTile(
            title: const Text('Versi Aplikasi'),
            leading: const Icon(Icons.info_outline),
            trailing: const Text(AppConstants.appVersion),
          ),
          ListTile(
            title: const Text('Tentang Aplikasi'),
            leading: const Icon(Icons.description),
            trailing: const Icon(Icons.chevron_right),
            onTap: () => _showAboutDialog(context),
          ),
          ListTile(
            title: const Text('Passing Grade 2024'),
            leading: const Icon(Icons.verified),
            trailing: const Icon(Icons.chevron_right),
            onTap: () => _showPassingGradeDialog(context),
          ),
          const SizedBox(height: 16),

          // Credit Banner
          AppUtils.buildCreditBanner(context),

          const SizedBox(height: 32),
        ],
      ),
        ),
      ),
    );
  }

  Widget _buildSectionHeader(String title) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(16, 16, 16, 8),
      child: Text(
        title,
        style: TextStyle(
          color: AppTheme.primaryRed,
          fontWeight: FontWeight.bold,
          fontSize: 13,
        ),
      ),
    );
  }

  Future<void> _selectTime(BuildContext context) async {
    final picked = await showTimePicker(
      context: context,
      initialTime: _selectedTime,
      builder: (context, child) {
        return Theme(
          data: Theme.of(context).copyWith(
            colorScheme: Theme.of(context).colorScheme.copyWith(
                  primary: AppTheme.primaryRed,
                ),
          ),
          child: child!,
        );
      },
    );

    if (picked != null) {
      setState(() => _selectedTime = picked);

      final settings = ref.read(userSettingsProvider);
      ref.read(userSettingsProvider.notifier).setDailyReminder(
            enabled: settings.dailyReminderEnabled,
            hour: picked.hour,
            minute: picked.minute,
          );
    }
  }

  void _showAboutDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Tentang TryOutCPNSbyIMAM'),
        content: const Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'TryOutCPNSbyIMAM adalah aplikasi latihan soal Seleksi Kompetensi Dasar (SKD) untuk persiapan ujian_cpns.',
            ),
            SizedBox(height: 12),
            Text(
              'Aplikasi ini membantu kamu berlatih soal TWK, TIU, dan TKP dengan fitur try out lengkap, latihan per subtopik, dan statistik progres.',
            ),
            SizedBox(height: 12),
            Text(
              '© 2024 TryOutCPNSbyIMAM',
              style: TextStyle(color: Colors.grey, fontSize: 12),
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Tutup'),
          ),
        ],
      ),
    );
  }

  void _showPassingGradeDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Passing Grade SKD 2024'),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            _buildGradeRow('TWK (Tes Wawasan Kebangsaan)', '≥ 65'),
            const SizedBox(height: 8),
            _buildGradeRow('TIU (Tes Intelegensi Umum)', '≥ 80'),
            const SizedBox(height: 8),
            _buildGradeRow('TKP (Tes Karakteristik Pribadi)', '≥ 166'),
            const SizedBox(height: 16),
            const Text(
              'Keterangan:',
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 4),
            const Text(
              'TWK & TIU: Benar = 5, Salah = 0\n'
              'TKP: Opsi A=5, B=4, C=3, D=2, E=1\n'
              '(Semua opsi situasiional, tidak ada jawaban salah mutlak)',
              style: TextStyle(fontSize: 12, color: Colors.grey),
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Tutup'),
          ),
        ],
      ),
    );
  }

  Future<void> _loadFontScale() async {
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      _fontScale = prefs.getDouble('font_scale') ?? 1.0;
    });
  }

  Future<void> _saveFontScale(double scale) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setDouble('font_scale', scale);
  }

  Widget _buildGradeRow(String label, String value) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Text(label),
        Text(
          value,
          style: const TextStyle(
            fontWeight: FontWeight.bold,
            color: AppTheme.primaryRed,
          ),
        ),
      ],
    );
  }
}
