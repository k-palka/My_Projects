# Generated by Django 2.2.11 on 2020-03-18 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0013_auto_20200318_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procedure',
            name='slug',
        ),
    ]