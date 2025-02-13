# Generated by Django 4.2 on 2024-04-02 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_course_enrollment_courses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='MALE', max_length=12),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='MALE', max_length=12),
        ),
    ]
