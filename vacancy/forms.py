from django import forms


class NewVacancyForm(forms.Form):
    description = forms.CharField(label='Description')
