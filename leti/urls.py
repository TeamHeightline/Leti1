from django.urls import path
from leti.views import *

app_name = 'leti'
urlpatterns = [
    path('students/create/', StudentsCreateView.as_view()),
    path('students/all/', StudentListView.as_view()),
    path('students/detail/<int:pk>/', StudentDetailView.as_view()),
    path('tusk/create/', TuskCreateView.as_view()),
    path('tusk/all', TuskListView.as_view()),
    path('tusk/detail/<int:pk>/', TuskDetailView.as_view()),
    path('teacher/create/', TeacherCreateView.as_view()),
    path('teaher/detail/<int:pk>/', TeacherDetailView.as_view()),
    path('question/create/', QuestionAndAnswerCreateView.as_view()),
    path('question/view/<int:pk>/', QuestionAndAnswersViewView.as_view()),
    path('question/pass/', CheckPassQuestionView.as_view()),
    path('question/saveresult/', save_tusk_result_view),
]
