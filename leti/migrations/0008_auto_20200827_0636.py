# Generated by Django 3.0.8 on 2020-08-27 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leti', '0007_auto_20200827_0609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passquestion',
            old_name='tusk_id',
            new_name='question_id',
        ),
    ]
