from django import forms

class Formulario(forms.Form):
    name = forms.CharField(max_length=90)
    email = forms.EmailField()
    website = forms.CharField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField()