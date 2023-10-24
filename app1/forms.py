from django import forms

class startform(forms.Form):
    name = forms.CharField(label="name", max_length=100)

class IndexForm(forms.Form):
    note = forms.CharField()    