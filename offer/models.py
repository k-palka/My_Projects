from django.db import models
from django.utils import timezone

# Create your models here.

DEPARTMENT = (
    ('OMiR', 'Oddział Modernizacji i Remontów'),
    ('WZP', 'Wydział Zamówień Publicznych'),
    ('PGK', 'Pion Głównego Księgowego'),
    ('DYREKTOR', 'Dyrektor'),
)

STATUS_CHOICES = (
    ('draft', 'Roboczy'),
    ('approved', 'Zatwierdzony'),
    ('rejected', 'Odrzucony'),
)

ROLE_CHOICES = (
    ('member', 'Członek Komisji'),
    ('secretary', 'Sekretarz'),
    ('chairman', 'Przewodniczący'),
    ('director', 'Dyrektor'),
)


class Employee(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    department = models.CharField(max_length=8, choices=DEPARTMENT, default='OMiR')


class Procedure(models.Model):
    numer = models.CharField(max_length=20)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateField(default=timezone.now)
    open = models.DateField(blank=True, null=True)
    close = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    employees = models.ManyToManyField(Employee, through='Role', through_fields=('procedure', 'employee'))

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title


class Role(models.Model):
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    roles = models.CharField(max_length=10,
                             choices=ROLE_CHOICES,
                             default='member')


class Offert(models.Model):
    submission = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    lead_time = models.PositiveIntegerField(help_text='w dniach')
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    votes = models.IntegerField(default=0)


class Company(models.Model):
    short_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=170)
    mail = models.EmailField()
    offert = models.ForeignKey(Offert, on_delete=models.CASCADE)
