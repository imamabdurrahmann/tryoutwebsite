import 'dart:io';
import 'dart:convert';

void main() {
  final files = ['twk','twk_2','twk_3','tiu','tiu_2','tiu_3','tkp','tkp_2','tkp_3'];
  for (final f in files) {
    final data = jsonDecode(File('assets/questions/$f.json').readAsStringSync()) as List;
    final first = data[0] as Map<String, dynamic>;
    final idKey = first.containsKey('questionId') ? 'questionId' : 'id';
    final textKey = first.containsKey('questionText') ? 'questionText' : 'question';
    
    // Check actual parsed IDs using Question.fromJson logic
    int validIds = 0;
    for (var q in data) {
      final id = q['id'] ?? q['questionId'] ?? '';
      if (id != null && id.toString().isNotEmpty) validIds++;
    }
    
    print('$f.json: keys=[$idKey, $textKey], total=${data.length}, validIds=$validIds');
  }
}
