# Generated by Django 2.1.8 on 2019-06-01 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20190601_0621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='user_id',
            new_name='user',
        ),
    ]
