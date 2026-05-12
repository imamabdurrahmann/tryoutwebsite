import 'dart:convert';
import 'dart:io';

void main() {
  final files = [
    'assets/questions/tiu.json',
    'assets/questions/tiu_2.json',
    'assets/questions/tiu_3.json',
    'assets/questions/twk.json',
    'assets/questions/twk_2.json',
    'assets/questions/twk_3.json',
    'assets/questions/tkp.json',
    'assets/questions/tkp_2.json',
    'assets/questions/tkp_3.json'
  ];

  final artifacts = [
    RegExp(r'Wait\b.*?Yes\.', caseSensitive: false, dotAll: true),
    RegExp(r'Wait\b.*', caseSensitive: false, dotAll: true),
    RegExp(r'Check\b.*', caseSensitive: false, dotAll: true),
  ];

  for (final file in files) {
    if (!File(file).existsSync()) continue;
    
    final content = File(file).readAsStringSync();
    final List<dynamic> questions = jsonDecode(content);
    bool modified = false;

    for (var q in questions) {
      if (q['explanation'] != null) {
        String expl = q['explanation'];
        String original = expl;
        
        for (final reg in artifacts) {
          expl = expl.replaceAll(reg, '');
        }
        
        // Trim and clean up trailing spaces or dots
        expl = expl.trim();
        if (expl.isNotEmpty && expl.endsWith(' .')) {
          expl = expl.substring(0, expl.length - 2) + '.';
        }
        
        if (expl != original) {
          q['explanation'] = expl;
          modified = true;
          print('Cleaned ${q['questionId']} in $file');
        }
      }
    }

    if (modified) {
      File(file).writeAsStringSync(jsonEncode(questions));
      print('Saved $file');
    }
  }
}
