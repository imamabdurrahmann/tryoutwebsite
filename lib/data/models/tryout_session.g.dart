// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'tryout_session.dart';

// **************************************************************************
// TypeAdapterGenerator
// **************************************************************************

class TryoutSessionAdapter extends TypeAdapter<TryoutSession> {
  @override
  final int typeId = 1;

  @override
  TryoutSession read(BinaryReader reader) {
    final numOfFields = reader.readByte();
    final fields = <int, dynamic>{
      for (int i = 0; i < numOfFields; i++) reader.readByte(): reader.read(),
    };
    return TryoutSession()
      ..sessionId = fields[0] as String
      ..packageType = fields[1] as String
      ..startTime = fields[2] as DateTime
      ..endTime = fields[3] as DateTime?
      ..durationSeconds = fields[4] as int
      ..answersJson = fields[5] as String
      ..flaggedQuestions = (fields[6] as List).cast<String>()
      ..totalScore = fields[7] as int
      ..twkScore = fields[8] as int
      ..tiuScore = fields[9] as int
      ..tkpScore = fields[10] as int
      ..twkPassed = fields[11] as bool
      ..tiuPassed = fields[12] as bool
      ..tkpPassed = fields[13] as bool
      ..overallPassed = fields[14] as bool
      ..twkCorrect = fields[15] as int
      ..tiuCorrect = fields[16] as int
      ..tkpAnswered = fields[17] as int
      ..twkWrong = fields[18] as int
      ..tiuWrong = fields[19] as int
      ..twkUnanswered = fields[20] as int
      ..tiuUnanswered = fields[21] as int
      ..tkpUnanswered = fields[22] as int
      ..twkQuestionCount = fields[23] as int
      ..tiuQuestionCount = fields[24] as int
      ..tkpQuestionCount = fields[25] as int;
  }

  @override
  void write(BinaryWriter writer, TryoutSession obj) {
    writer
      ..writeByte(26)
      ..writeByte(0)
      ..write(obj.sessionId)
      ..writeByte(1)
      ..write(obj.packageType)
      ..writeByte(2)
      ..write(obj.startTime)
      ..writeByte(3)
      ..write(obj.endTime)
      ..writeByte(4)
      ..write(obj.durationSeconds)
      ..writeByte(5)
      ..write(obj.answersJson)
      ..writeByte(6)
      ..write(obj.flaggedQuestions)
      ..writeByte(7)
      ..write(obj.totalScore)
      ..writeByte(8)
      ..write(obj.twkScore)
      ..writeByte(9)
      ..write(obj.tiuScore)
      ..writeByte(10)
      ..write(obj.tkpScore)
      ..writeByte(11)
      ..write(obj.twkPassed)
      ..writeByte(12)
      ..write(obj.tiuPassed)
      ..writeByte(13)
      ..write(obj.tkpPassed)
      ..writeByte(14)
      ..write(obj.overallPassed)
      ..writeByte(15)
      ..write(obj.twkCorrect)
      ..writeByte(16)
      ..write(obj.tiuCorrect)
      ..writeByte(17)
      ..write(obj.tkpAnswered)
      ..writeByte(18)
      ..write(obj.twkWrong)
      ..writeByte(19)
      ..write(obj.tiuWrong)
      ..writeByte(20)
      ..write(obj.twkUnanswered)
      ..writeByte(21)
      ..write(obj.tiuUnanswered)
      ..writeByte(22)
      ..write(obj.tkpUnanswered)
      ..writeByte(23)
      ..write(obj.twkQuestionCount)
      ..writeByte(24)
      ..write(obj.tiuQuestionCount)
      ..writeByte(25)
      ..write(obj.tkpQuestionCount);
  }

  @override
  int get hashCode => typeId.hashCode;

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is TryoutSessionAdapter &&
          runtimeType == other.runtimeType &&
          typeId == other.typeId;
}
