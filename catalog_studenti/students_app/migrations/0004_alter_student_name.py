# Generated by Django 3.2.9 on 2021-12-03 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0003_student_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
