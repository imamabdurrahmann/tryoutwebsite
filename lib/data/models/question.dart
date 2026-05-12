import 'dart:convert';
import 'package:hive/hive.dart';

part 'question.g.dart';

@HiveType(typeId: 0)
class Question extends HiveObject {
  @HiveField(0)
  late String questionId;

  @HiveField(1)
  late String category;

  @HiveField(2)
  late String subcategory;

  @HiveField(3)
  late String questionText;

  @HiveField(4)
  late List<String> options;

  @HiveField(5)
  late String answer;

  @HiveField(6)
  late String explanation;

  @HiveField(7)
  late String difficulty;

  @HiveField(8)
  late bool isFigural;

  @HiveField(9)
  String? figuralData;

  Question();

  Question.create({
    required this.questionId,
    required this.category,
    required this.subcategory,
    required this.questionText,
    required this.options,
    required this.answer,
    required this.explanation,
    required this.difficulty,
    this.isFigural = false,
    this.figuralData,
  });

  factory Question.fromJson(Map<String, dynamic> json) {
    // Handle JSON files with different key names (questionId vs id, questionText vs question)
    final id = json['id'] as String? ?? json['questionId'] as String? ?? '';
    final text = json['question'] as String? ?? json['questionText'] as String? ?? '';

    // Handle options format: bisa List<String> atau List<Map> dengan {key, text}
    List<String> options;
    final rawOptions = json['options'];
    if (rawOptions is List) {
      // Cek apakah options adalah List<String> atau List<Map>
      if (rawOptions.isNotEmpty && rawOptions.first is Map) {
        // Format object: [{key: "A", text: "..."}, ...] — ambil property 'text'
        options = rawOptions.map((opt) {
          if (opt is Map) {
            return opt['text']?.toString() ?? opt['key']?.toString() ?? '';
          }
          return opt.toString();
        }).toList();
      } else {
        // Format string: ["Option A", "Option B", ...]
        options = rawOptions.map((opt) => opt.toString()).toList();
      }
    } else {
      options = [];
    }

    return Question.create(
      questionId: id,
      category: json['category'] as String? ?? '',
      subcategory: json['subcategory'] as String? ?? '',
      questionText: text,
      options: options,
      answer: json['answer'] as String? ?? '',
      explanation: json['explanation'] as String? ?? '',
      difficulty: json['difficulty'] as String? ?? 'medium',
      isFigural: json['isFigural'] as bool? ?? false,
      figuralData: _parseFiguralData(json['figuralData']),
    );
  }

  /// figuralData bisa String atau Map — handle keduanya.
  static String? _parseFiguralData(dynamic val) {
    if (val == null) return null;
    if (val is String) return val;
    if (val is Map) {
      // Simpan sebagai JSON string agar konsisten dengan schema String?
      return jsonEncode(val);
    }
    return val.toString();
  }

  Map<String, dynamic> toJson() => {
        'id': questionId,
        'category': category,
        'subcategory': subcategory,
        'question': questionText,
        'options': options,
        'answer': answer,
        'explanation': explanation,
        'difficulty': difficulty,
        'isFigural': isFigural,
        'figuralData': figuralData,
      };

  String getOptionLabel(int index) {
    const labels = ['A', 'B', 'C', 'D', 'E'];
    if (index >= 0 && index < labels.length) {
      return labels[index];
    }
    return '';
  }

  int getOptionIndex(String label) {
    return ['A', 'B', 'C', 'D', 'E'].indexOf(label);
  }
}
