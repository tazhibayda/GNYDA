# Generated by Django 4.0 on 2022-05-08 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_alter_course_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='liked',
        ),
    ]
