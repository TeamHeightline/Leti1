# Generated by Django 3.0.8 on 2020-08-26 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leti', '0003_auto_20200826_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionandanswers',
            name='answer_1',
            field=models.CharField(max_length=200, verbose_name='Вопрос 1'),
        ),
        migrations.AlterField(
            model_name='questionandanswers',
            name='answer_1_is',
            field=models.BooleanField(verbose_name='Правильность ответа'),
        ),
        migrations.AlterField(
            model_name='questionandanswers',
            name='answer_2',
            field=models.CharField(max_length=200, verbose_name='Вопрос 2'),
        ),
        migrations.AlterField(
            model_name='questionandanswers',
            name='answer_2_is',
            field=models.BooleanField(verbose_name='Правильность ответа'),
        ),
        migrations.AlterField(
            model_name='questionandanswers',
            name='answer_3',
            field=models.CharField(max_length=200, verbose_name='Вопрос 3'),
        ),
        migrations.AlterField(
            model_name='questionandanswers',
            name='answer_3_is',
            field=models.BooleanField(verbose_name='Правильность ответа'),
        ),
        migrations.AlterField(
            model_name='questionandanswers',
            name='answer_4',
            field=models.CharField(max_length=200, verbose_name='Вопрос 4'),
        ),
        migrations.AlterField(
            model_name='questionandanswers',
            name='answer_4_is',
            field=models.BooleanField(verbose_name='Правильность ответа'),
        ),
        migrations.AlterField(
            model_name='questionandanswers',
            name='answer_5',
            field=models.CharField(max_length=200, verbose_name='Вопрос 5'),
        ),
        migrations.AlterField(
            model_name='questionandanswers',
            name='answer_5_is',
            field=models.BooleanField(verbose_name='Правильность ответа'),
        ),
        migrations.AlterField(
            model_name='questionandanswers',
            name='answer_6',
            field=models.CharField(max_length=200, verbose_name='Вопрос 6'),
        ),
        migrations.AlterField(
            model_name='questionandanswers',
            name='answer_6_is',
            field=models.BooleanField(verbose_name='Правильность ответа'),
        ),
        migrations.AlterField(
            model_name='questionandanswers',
            name='question_text',
            field=models.TextField(verbose_name='Текст вопроса'),
        ),
    ]
