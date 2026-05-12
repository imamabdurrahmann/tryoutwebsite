import 'dart:io';
import 'dart:convert';

void main() {
  final files = ['twk','twk_2','twk_3','tiu','tiu_2','tiu_3','tkp','tkp_2','tkp_3'];
  for (final f in files) {
    try {
      final data = jsonDecode(File('assets/questions/$f.json').readAsStringSync()) as List;
      final cats = data.map((q) => q['category']).toSet();
      final ids = data.map((q) => q['questionId']).toSet();
      print('$f: ${data.length} soal, categories=$cats, unique_ids=${ids.length}');
    } catch(e) {
      print('$f: ERROR $e');
    }
  }
}
