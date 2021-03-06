# Generated by Django 3.0.4 on 2020-03-09 18:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('member', 'Członek Komisji'), ('secretary', 'Sekretarz'), ('chairman', 'Przewodniczący'), ('director', 'Dyrektor')], default='member', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numer', models.CharField(max_length=14)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('publish', models.DateField(default=django.utils.timezone.now)),
                ('open', models.DateTimeField(blank=True, null=True)),
                ('close', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('draft', 'Roboczy'), ('approved', 'Zatwierdzony'), ('rejected', 'Odrzucony')], default='draft', max_length=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.Employee')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
        migrations.CreateModel(
            name='Offert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission', models.DateTimeField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lead_time', models.PositiveIntegerField(help_text='w dniach')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('votes', models.IntegerField(default=0)),
                ('procedure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.Procedure')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=170)),
                ('mail', models.EmailField(max_length=254)),
                ('offert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.Offert')),
            ],
        ),
    ]
