from django import forms
from .models import *


class AddProcedureForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = '__all__'
