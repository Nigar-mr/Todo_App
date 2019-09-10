# Generated by Django 2.2.5 on 2019-09-07 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0008_post_add_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='add_list',
        ),
        migrations.CreateModel(
            name='AddList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_list', models.CharField(max_length=50)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_app.Post')),
            ],
        ),
    ]