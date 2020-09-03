from leti.models import *


def save_test_result(student_id: int, tusk_id: int, right_q: int):
    s = StudentDidTusk(student_id=student_id, tusk_id=tusk_id, true_false_percent=100 * (right_q / 6))
    s.save()


# Модуль, узнающий правильные ответы для этого конкретного вопроса
def get_question_nom_of_true_answers(question_id: int) -> list:
    r = []
    question = QuestionAndAnswers.objects.all().filter(question_id=question_id).values()[0]
    if question['answer_1_is']:
        r.append(1)
    if question['answer_2_is']:
        r.append(2)
    if question['answer_3_is']:
        r.append(3)
    if question['answer_4_is']:
        r.append(4)
    if question['answer_5_is']:
        r.append(5)
    if question['answer_6_is']:
        r.append(6)
    return r


# Модуль получает те номера вопроов, которые студент посчитал правильными
def student_version_of_true_answer(request) -> list:
    student_version_of_true_answers = []
    for key in request.data:
        if str(key)[0:13] == 'right_or_not_':
            student_version_of_true_answers.append(int(str(key)[13]))
    return student_version_of_true_answers


# Ну... здесь происходит высшая математика берем список ответа пользователя, и правильный список ответов,
# ищем пересечения, делем пересечения на кол-во правильных и узнаем процент правильных ответов


def check_pass_question(request) -> int:
    a = student_version_of_true_answer(request)
    b = get_question_nom_of_true_answers(request.data['question_id'])
    interception = list(set(a) & set(b))
    return int((len(interception) / len(b)) * 100)
