# Generated by Django 4.2.16 on 2024-11-13 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_remove_file_owner_file_content_type_file_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='content_type',
            field=models.CharField(max_length=50),
        ),
    ]
