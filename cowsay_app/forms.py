from django import forms
from cowsay_app.models import Input

class InputForm(forms.Form):
    input = forms.CharField(max_length=80)