# Generated by Django 2.2.11 on 2020-03-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0017_auto_20200321_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='rates',
            field=models.CharField(choices=[('PRZYJMUJĘ', 'OK'), ('ODRZUCAM', 'NIE OK')], default=None, max_length=20),
        ),
    ]
