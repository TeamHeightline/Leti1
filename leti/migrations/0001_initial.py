# Generated by Django 3.0.8 on 2020-08-21 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('course', models.SmallIntegerField(verbose_name='Номер курса')),
            ],
        ),
        migrations.CreateModel(
            name='Tusk',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Айди задания')),
                ('tusk_name', models.CharField(max_length=80, verbose_name='Название задания')),
                ('urls', models.URLField(verbose_name='Ссылка на лекцию')),
                ('text', models.CharField(max_length=1024, verbose_name='Текст задания')),
                ('previous_tusk', models.URLField(null=True, verbose_name='Прошлый номер')),
                ('next_tusk', models.URLField(null=True, verbose_name='Следующий номер')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leti.Student')),
            ],
        ),
    ]
