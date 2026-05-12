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
    
    print('--- $file ---');
    final content = File(file).readAsStringSync();
    final List<dynamic> questions = jsonDecode(content);
    
    for (var q in questions) {
      if (q['subcategory'] == 'Figural' || q['type'] == 'figural') {
        print('ID: ${q['id']}');
        print('Type: ${q['type']}');
        print('Explanation: ${q['explanation']}');
        print('Grid: ${q['gridShapes']}');
        print('Answers: ${q['answerShapes']}');
        print('Correct Index: ${q['correctIndex']}');
        print('----------------------');
      }
    }
  }
}
