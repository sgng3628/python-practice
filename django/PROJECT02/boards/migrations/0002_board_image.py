# Generated by Django 2.1.8 on 2019-05-22 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
