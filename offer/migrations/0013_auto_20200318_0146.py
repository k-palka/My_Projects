# Generated by Django 2.2.11 on 2020-03-18 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0012_auto_20200318_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedure',
            name='status',
            field=models.CharField(choices=[('roboczy', 'Roboczy'), ('zatwierdzony', 'Zatwierdzony'), ('odrzucony', 'Odrzucony')], default='draft', max_length=20),
        ),
    ]
