# Generated by Django 2.2.11 on 2020-03-18 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0011_auto_20200317_1113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offert',
            options={'ordering': ('submission',)},
        ),
    ]
