# Generated by Django 3.2.4 on 2021-07-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_alter_sale_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='csv',
            name='csv_file',
            field=models.FileField(null=True, upload_to='csv'),
        ),
        migrations.AlterField(
            model_name='csv',
            name='file_name',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
