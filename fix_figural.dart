import 'dart:convert';
import 'dart:io';

void main() {
  final Map<String, List<String>> manualAnswers = {
    'tiu_013': ["blue-circle-empty", "red-triangle", "green-square", "blue-circle", "red-triangle"],
    'tiu_018': ["black-arrow_down", "black-arrow_left", "black-arrow_up", "red-arrow_right", "red-arrow_up"],
    'tiu_025': ["blue-triangle", "red-triangle", "green-square", "blue-triangle", "red-square"],
    'tiu_032': ["blue-square", "red-triangle", "blue-square", "green-circle", "red-triangle"],
    'tiu_2_034': ["blue-square", "red-circle", "green-triangle", "blue-square", "green-circle"],
    'tiu_2_035': ["black-diamond", "black-circle-empty", "black-square", "black-square", "black-diamond"],
    'tiu3_031': ["black-square", "black-circle", "black-triangle", "black-square", "black-circle"],
    'tiu3_032': ["black-square", "black-circle-empty", "black-triangle", "black-square-empty", "black-circle"],
    'tiu3_033': ["black-square", "black-circle-empty", "black-triangle-empty", "black-triangle", "black-circle"],
    'tiu3_034': ["blue-square", "green-triangle", "red-circle", "green-circle", "red-circle"],
    'tiu3_035': ["black-arrow_up", "black-arrow_down", "black-arrow_right", "black-arrow_left", "black-arrow_up"],
  };

  final files = [
    'assets/questions/tiu.json',
    'assets/questions/tiu_2.json',
    'assets/questions/tiu_3.json'
  ];

  for (final file in files) {
    if (!File(file).existsSync()) continue;
    
    final content = File(file).readAsStringSync();
    final List<dynamic> questions = jsonDecode(content);
    bool modified = false;

    for (var q in questions) {
      if (q['subcategory'] == 'Figural' || q['type'] == 'figural') {
        final qId = q['questionId'] ?? q['id'];
        if (manualAnswers.containsKey(qId)) {
          dynamic fd = q['figuralData'];
          Map<String, dynamic> fdMap;
          bool isString = false;
          
          if (fd == null) {
            fdMap = {};
          } else if (fd is String) {
            fdMap = jsonDecode(fd);
            isString = true;
          } else if (fd is Map) {
            fdMap = fd as Map<String, dynamic>;
          } else {
            fdMap = {};
          }

          fdMap['answerShapes'] = manualAnswers[qId];
          
          if (isString) {
            q['figuralData'] = jsonEncode(fdMap);
          } else {
            q['figuralData'] = fdMap;
          }
          
          modified = true;
          print('Updated $qId');
        }
      }
    }

    if (modified) {
      File(file).writeAsStringSync(jsonEncode(questions));
      print('Saved $file');
    }
  }
}
