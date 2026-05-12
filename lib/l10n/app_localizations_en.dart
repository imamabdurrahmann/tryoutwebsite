// ignore: unused_import
import 'package:intl/intl.dart' as intl;
import 'app_localizations.dart';

// ignore_for_file: type=lint

/// The translations for English (`en`).
class AppLocalizationsEn extends AppLocalizations {
  AppLocalizationsEn([String locale = 'en']) : super(locale);

  @override
  String get appTitle => 'TryOutCPNSbyIMAM';

  @override
  String get home => 'Home';

  @override
  String get tryout => 'Try Out';

  @override
  String get history => 'History';

  @override
  String get profile => 'Profile';

  @override
  String get practice => 'Practice';

  @override
  String get start => 'Start';

  @override
  String get cancel => 'Cancel';

  @override
  String get confirm => 'Confirm';

  @override
  String get submit => 'Submit';

  @override
  String get finish => 'Finish';

  @override
  String get next => 'Next';

  @override
  String get previous => 'Previous';

  @override
  String question(int number, int total) {
    return 'Question $number of $total';
  }

  @override
  String get totalScore => 'Total Score';

  @override
  String get passingGrade => 'Passing Grade';

  @override
  String get lulus => 'PASSED';

  @override
  String get tidakLulus => 'NOT PASSED';

  @override
  String get correct => 'Correct';

  @override
  String get wrong => 'Wrong';

  @override
  String get unanswered => 'Unanswered';

  @override
  String get explanation => 'Explanation';

  @override
  String get seeReview => 'See Review';

  @override
  String get tryAgain => 'Try Again';

  @override
  String get backToHome => 'Back to Home';

  @override
  String get darkMode => 'Dark Mode';

  @override
  String get dailyReminder => 'Daily Reminder';

  @override
  String get reminderTime => 'Reminder Time';

  @override
  String get settings => 'Settings';

  @override
  String get about => 'About';

  @override
  String get version => 'Version';

  @override
  String get tryOutComplete => 'Complete Try Out';

  @override
  String get practiceTKW => 'TWK Practice';

  @override
  String get practiceTIU => 'TIU Practice';

  @override
  String get practiceTKP => 'TKP Practice';

  @override
  String get practiceByTopic => 'Practice by Topic';
}
