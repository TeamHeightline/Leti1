from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    course = models.SmallIntegerField(verbose_name='Номер курса')


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)


class Tusk(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Айди задания')
    tusk_name = models.CharField(max_length=80, verbose_name='Название задания')
    creator = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    urls = models.URLField(verbose_name='Ссылка на лекцию')
    text = models.TextField(verbose_name='Текст задания')
    previous_tusk = models.URLField(verbose_name='Прошлый номер', null=True)
    next_tusk = models.URLField(verbose_name='Следующий номер', null=True)

# Модель для хранения всех результатов тестов конкретного пользователя


class StudentDidTusk(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    tusk_id = models.ForeignKey(Tusk, on_delete=models.CASCADE)
    true_false_percent = models.IntegerField()


# Мы отдельно храним каждый ворос, и варианты ответа на него(6 штук), затем в моделе Test хроним массив айдишников
# вопросов

# Моделька для создания и показа вопроса, (тест состоит из нескольких вопросов)
class QuestionAndAnswers(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.TextField(verbose_name='Текст вопроса')
    answer_1 = models.CharField(max_length=200, verbose_name='Вопрос 1')
    answer_1_is = models.BooleanField(verbose_name='Правильность ответа')
    answer_2 = models.CharField(max_length=200, verbose_name='Вопрос 2')
    answer_2_is = models.BooleanField(verbose_name='Правильность ответа')
    answer_3 = models.CharField(max_length=200, verbose_name='Вопрос 3')
    answer_3_is = models.BooleanField(verbose_name='Правильность ответа')
    answer_4 = models.CharField(max_length=200, verbose_name='Вопрос 4')
    answer_4_is = models.BooleanField(verbose_name='Правильность ответа')
    answer_5 = models.CharField(max_length=200, verbose_name='Вопрос 5')
    answer_5_is = models.BooleanField(verbose_name='Правильность ответа')
    answer_6 = models.CharField(max_length=200, verbose_name='Вопрос 6')
    answer_6_is = models.BooleanField(verbose_name='Правильность ответа')

# Моделька в которой будут собираться список вопросов одного теста


class Test(models.Model):
    test_id = models.AutoField(primary_key=True, verbose_name='Айди теста')
    questions = models.ManyToManyField(QuestionAndAnswers)

# Моделька в которой хранится сколько правильных ответов дал студент на ОДИН из вопросов


class TestProgress(models.Model):
    progress_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    tusk_id = models.ForeignKey(QuestionAndAnswers, on_delete=models.CASCADE)
    kol_user_true_answer = models.IntegerField(
        verbose_name='Колличество правильных ответов, которые сделал пользователь')


class PassQuestion(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    question_id = models.ForeignKey(QuestionAndAnswers, on_delete=models.CASCADE)
    right_or_not_1 = models.BooleanField(default=False)
    right_or_not_2 = models.BooleanField(default=False)
    right_or_not_3 = models.BooleanField(default=False)
    right_or_not_4 = models.BooleanField(default=False)
    right_or_not_5 = models.BooleanField(default=False)
    right_or_not_6 = models.BooleanField(default=False)
