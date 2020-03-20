from django import forms
from .models import *
from django.forms import ModelForm, Textarea
from django.forms.models import inlineformset_factory
from django.utils import timezone


# class AddProcedureForm(forms.ModelForm):
#     numer = forms.CharField(max_length=20)
#     title = forms.CharField(max_length=250)
#     publish = forms.DateField()
#     open = forms.DateField()
#     close = forms.DateField()
#     status = forms.ChoiceField(choices=STATUS_CHOICES)

    # class Meta:
    #     model = Procedure
    #     fields = '__all__'
