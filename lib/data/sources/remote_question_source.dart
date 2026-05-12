import 'package:dio/dio.dart';
import '../../core/constants/app_constants.dart';
import '../models/question.dart';

class RemoteQuestionSource {
  final Dio _dio;

  RemoteQuestionSource() : _dio = Dio(BaseOptions(
    baseUrl: AppConstants.apiBaseUrl,
    connectTimeout: const Duration(seconds: 10),
    receiveTimeout: const Duration(seconds: 30),
  ));

  /// Cek versi soal terbaru dari server
  Future<String?> checkVersion() async {
    try {
      final response = await _dio.get(AppConstants.apiQuestionsVersion);
      if (response.statusCode == 200) {
        return response.data['version'] as String?;
      }
    } catch (_) {
      // Offline atau error - ignore
    }
    return null;
  }

  /// Download semua soal dari server
  Future<List<Question>> downloadQuestions() async {
    try {
      final response = await _dio.get(AppConstants.apiQuestions);
      if (response.statusCode == 200) {
        final List<dynamic> data = response.data['questions'];
        return data.map((json) => Question.fromJson(json)).toList();
      }
    } catch (_) {
      // Error handling
    }
    return [];
  }

  /// Download soal per kategori
  Future<List<Question>> downloadQuestionsByCategory(String category) async {
    try {
      final response = await _dio.get(
        '${AppConstants.apiQuestions}/$category',
      );
      if (response.statusCode == 200) {
        final List<dynamic> data = response.data['questions'];
        return data.map((json) => Question.fromJson(json)).toList();
      }
    } catch (_) {
      // Error handling
    }
    return [];
  }
}
