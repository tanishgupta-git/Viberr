# Generated by Django 3.0.8 on 2020-09-17 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20200916_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default='', upload_to='music/songs'),
        ),
    ]