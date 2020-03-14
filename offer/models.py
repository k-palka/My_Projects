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
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    department = models.CharField(max_length=8, choices=DEPARTMENT, default='OMiR')

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name


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
        return f"{self.numer} {self.title}"


class Role(models.Model):
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    roles = models.CharField(max_length=10,
                             choices=ROLE_CHOICES,
                             default='member')


class Offert(models.Model):
    submission = models.DateField(blank=True, null=True)
    company_name = models.CharField(max_length=70, default='firma')
    company_address = models.CharField(max_length=170, default='adres firmy')
    company_mail = models.EmailField(default='mail@wp.pl')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    lead_time = models.PositiveIntegerField(help_text='w dniach')
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
