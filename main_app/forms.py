from django import forms
from .models import Movement


class MovementForm(forms.ModelForm):
    class Meta:
        model = Movement
        fields = ['name', 'author', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'author': forms.TextInput(attrs={'class': 'input'}),
            'image': forms.FileInput(
                attrs={'class': 'input input--image'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64,
                               widget=forms.TextInput(
                                   attrs={'class': 'input'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input'}))
