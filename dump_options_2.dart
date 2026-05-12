import 'dart:convert';
import 'dart:io';

void main() {
  final files = [
    'assets/questions/tiu.json',
    'assets/questions/tiu_2.json',
    'assets/questions/tiu_3.json'
  ];

  for (final file in files) {
    if (!File(file).existsSync()) continue;
    
    final content = File(file).readAsStringSync();
    final List<dynamic> questions = jsonDecode(content);
    
    for (var q in questions) {
      if (q['subcategory'] == 'Figural') {
        print('ID: ${q['questionId']}');
        List<dynamic> options = q['options'];
        for (var opt in options) {
          print('  $opt');
        }
      }
    }
  }
}
