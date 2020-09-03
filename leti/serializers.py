from rest_framework import serializers
from .models import *


class StudentViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'course')


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'course')


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TuskViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tusk
        fields = ('id', 'tusk_name', 'creator')


class TuskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tusk
        fields = '__all__'


class TuskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tusk
        fields = '__all__'


class TeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class SaveTuskResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDidTusk
        fields = '__all__'


class QuestionAndAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAndAnswers
        fields = '__all__'


# Отправляем только текст и варианты ответа, не дай бог сказать, какие из ответов правильные
# Хорошо бы рандомезировать порядок ответов, а их истинность и ложность будем проверять прямым сравнением,
# когда пользователь пришлет свой ответ, либо будем сохранять в отдельную лайв модель номера правильных
# ответов для этого конкретного вопроса, хотя второй вариант явно сверх проблемотичен


class QuestionAndAnswersViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAndAnswers
        fields = ('question_text', 'answer_1', 'answer_2', 'answer_3', 'answer_4', 'answer_5', 'answer_6')


class PassQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassQuestion
        fields = '__all__'

