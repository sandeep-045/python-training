# Generated by Django 3.2.4 on 2021-07-09 07:42

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=10)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tag',
            field=models.ManyToManyField(to='myapp.Tag'),
        ),
        migrations.AddField(
            model_name='review',
            name='tag',
            field=models.ManyToManyField(to='myapp.Tag'),
        ),
    ]