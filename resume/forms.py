from django import forms


class NewResumeForm(forms.Form):
    description = forms.CharField(label='Description')

