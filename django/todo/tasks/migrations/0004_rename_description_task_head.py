# Generated by Django 3.2.4 on 2021-06-28 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_rename_title_task_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='description',
            new_name='head',
        ),
    ]
