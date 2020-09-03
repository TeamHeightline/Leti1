# from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from leti.serializers import *
from rest_framework import filters
from .services import *


# Create your views here.

class StudentsCreateView(generics.CreateAPIView):
    serializer_class = StudentCreateSerializer
    queryset = Student.objects.all()


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentDetailSerializer
    queryset = Student.objects.all()


class StudentListView(generics.ListAPIView):
    serializer_class = StudentViewSerializer
    queryset = Student.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class TuskCreateView(generics.CreateAPIView):
    serializer_class = TuskCreateSerializer
    queryset = Tusk.objects.all()


class TuskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TuskDetailSerializer
    queryset = Tusk.objects.all()


class TuskListView(generics.ListAPIView):
    serializer_class = TuskViewSerializer
    queryset = Tusk.objects.all()


class TeacherCreateView(generics.CreateAPIView):
    serializer_class = TeacherCreateSerializer
    queryset = Teacher.objects.all()


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherDetailSerializer
    queryset = Teacher.objects.all()


@api_view(['POST'])
def save_tusk_result_view(request):
    serializer_class = SaveTuskResultSerializer(data=request.data)
    queryset = StudentDidTusk.objects.all()
    student_id = request.GET.get('student_id')
    tusk_id = request.GET.get('tusk_id')
    right_q = request.Get.get('right_q')
    save_test_result(student_id, tusk_id, right_q)
    return JsonResponse({'success': True})


class QuestionAndAnswerCreateView(generics.CreateAPIView):
    serializer_class = QuestionAndAnswersSerializer
    queryset = QuestionAndAnswers.objects.all()


class QuestionAndAnswersViewView(generics.RetrieveAPIView):
    serializer_class = QuestionAndAnswersViewSerializer
    queryset = QuestionAndAnswers.objects.all()


class CheckPassQuestionView(APIView):
    serializer_class = PassQuestionSerializer
    queryset = PassQuestion.objects.all()

    def post(self, request, format=None):
        try:
            true_percent = check_pass_question(request)
        except Exception as e:
            true_percent = 'Sorry someone going to die ' + str(e)
        return Response(true_percent)
