from django import forms
from .models import *
from django.forms import ModelForm, Textarea
from django.forms.models import inlineformset_factory


class AddProcedureForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = '__all__'

