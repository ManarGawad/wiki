from django import forms
from django.core.exceptions import ValidationError
from . import util


class SearchForm(forms.Form):
    page = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control-sm'}))


class CreatePage(forms.Form):
    title = forms.CharField(label="Title", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label="Content", required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))

class Edit(forms.Form):
    new_content = forms.CharField(label="Content", required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
