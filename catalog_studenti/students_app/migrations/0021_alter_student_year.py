# Generated by Django 4.0.2 on 2022-03-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0020_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(choices=[('1', 'YEAR 1'), ('2', 'YEAR 2'), ('3', 'YEAR 3'), ('0', 'TEACHER')], max_length=20),
        ),
    ]
