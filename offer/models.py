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
    ('roboczy', 'Roboczy'),
    ('zatwierdzony', 'Zatwierdzony'),
    ('odrzucony', 'Odrzucony'),
)

ROLE_CHOICES = (
    ('Członek Komisji', 'Członek Komisji'),
    ('Sekretarz', 'Sekretarz'),
    ('Przewodniczący', 'Przewodniczący'),
    ('Dyrektor', 'Dyrektor'),
)

RATES_CHOICES = (
    ('PRZYJMUJĘ', 'OK'),
    ('ODRZUCAM', 'NIE OK')
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
    # slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateField(default=timezone.now)
    open = models.DateField(blank=True, null=True)
    close = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20,
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
    roles = models.CharField(max_length=20,
                             choices=ROLE_CHOICES,
                             default='member')

    class Meta:
        ordering = ('procedure',)

    def __str__(self):
        return f"{self.roles} {self.employee}"


class Offert(models.Model):
    submission = models.DateField(blank=True, null=True)
    company_name = models.CharField(max_length=70, default='firma')
    company_address = models.CharField(max_length=170, default='adres firmy')
    company_mail = models.EmailField(default='mail@wp.pl')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    lead_time = models.PositiveIntegerField(help_text='w dniach')
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('submission',)

    def __str__(self):
        return f"{self.submission} {self.procedure.numer} {self.company_name}"


class Evaluation(models.Model):
    offert = models.ForeignKey(Offert, on_delete=models.CASCADE)
    author = models.CharField(max_length=80)
    comment_text = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rates = models.CharField(max_length=20,
                             choices=RATES_CHOICES,
                             default=None)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '{} {} {}'.format(self.created, self.author, self.comment_text)
