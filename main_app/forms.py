from django import forms
from .models import Movement


class MovementForm(forms.ModelForm):
    class Meta:
        model = Movement
        fields = ['name', 'author', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'data-validation-name': 'name'}),
            'author': forms.TextInput(attrs={'class': 'input', 'data-validation-name': 'author'}),
            'image': forms.FileInput(
                attrs={'class': 'input input--image'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64,
                               widget=forms.TextInput(
                                   attrs={'class': 'input', 'data-validation-name': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input', 'data-validation-name': 'password'}))
