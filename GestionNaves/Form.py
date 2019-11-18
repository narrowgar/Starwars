from django import forms

class Formulario(forms.Form):
    website = forms.CharField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField()