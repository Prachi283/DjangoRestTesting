# Generated by Django 4.0.2 on 2022-03-07 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='last_modified',
        ),
        migrations.AlterField(
            model_name='todo',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
    ]