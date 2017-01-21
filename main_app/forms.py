from django import forms
from .models import Movement


class MovementForm(forms.ModelForm):
    class Meta:
        model = Movement
        fields = ['name', 'author', 'image']


class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
