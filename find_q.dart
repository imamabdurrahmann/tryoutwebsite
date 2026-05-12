import 'dart:io';
import 'dart:convert';

void main() {
  final file = File('assets/questions/tiu_3.json');
  final data = jsonDecode(file.readAsStringSync()) as List;
  
  // Fix tiu3_034 (index 33): answer E->A, correctIndex 4->0
  final q = data[33] as Map<String, dynamic>;
  print('BEFORE: id=${q['id']}, answer=${q['answer']}');
  
  // Fix answer
  q['answer'] = 'A';
  
  // Fix correctIndex in figuralData
  final fd = q['figuralData'];
  if (fd is Map) {
    fd['correctIndex'] = 0;
  } else if (fd is String) {
    final parsed = jsonDecode(fd) as Map<String, dynamic>;
    parsed['correctIndex'] = 0;
    q['figuralData'] = parsed; // store as Map (will be encoded)
  }
  
  print('AFTER: id=${q['id']}, answer=${q['answer']}');
  
  // Write back
  final encoder = JsonEncoder.withIndent('  ');
  file.writeAsStringSync(encoder.convert(data));
  print('Saved tiu_3.json');
}
