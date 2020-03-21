from django import forms
from .models import *


class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = '__all__'

class ProcedureForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = '__all__'

class OffertForm(forms.ModelForm):
    class Meta:
        model = Offert
        fields = '__all__'