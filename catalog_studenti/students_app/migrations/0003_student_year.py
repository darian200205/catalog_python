# Generated by Django 3.2.9 on 2021-12-03 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0002_rename_updated_student_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1),
            preserve_default=False,
        ),
    ]
