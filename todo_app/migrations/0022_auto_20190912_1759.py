# Generated by Django 2.2.5 on 2019-09-12 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0021_auto_20190912_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='user',
        ),
    ]
