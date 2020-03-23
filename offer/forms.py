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


class LoginForm(forms.Form):
    login = forms.CharField(label='login', max_length=120, required=False)
    password = forms.CharField(label='password', max_length=120,
                               widget=forms.PasswordInput)
