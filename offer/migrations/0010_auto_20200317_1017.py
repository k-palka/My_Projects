# Generated by Django 2.2.11 on 2020-03-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0009_auto_20200314_2123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='role',
            options={'ordering': ('procedure',)},
        ),
        migrations.AlterField(
            model_name='procedure',
            name='status',
            field=models.CharField(choices=[('roboczy', 'Roboczy'), ('zatwierdzony', 'Zatwierdzony'), ('odrzucony', 'Odrzucony')], default='draft', max_length=10),
        ),
        migrations.AlterField(
            model_name='role',
            name='roles',
            field=models.CharField(choices=[('Członek Komisji', 'Członek Komisji'), ('Sekretarz', 'Sekretarz'), ('Przewodniczący', 'Przewodniczący'), ('Dyrektor', 'Dyrektor')], default='member', max_length=10),
        ),
    ]