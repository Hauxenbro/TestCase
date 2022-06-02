from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Cards


class AddCard(forms.ModelForm):
    class Meta:
        model = Cards
        fields = ('seria', 'number', 'finish_date')
        widgets = {
            'seria':forms.TextInput(attrs={'class':'form-control'}),
            'number':forms.NumberInput(attrs={'class':'form-control'}),
            'finish_date': forms.DateTimeInput(attrs={'class':'form-control'}),
        }

class EditForm(forms.Form):
    seria = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    finish_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'form-control'}))


class AddUser(UserCreationForm):
    email = forms.EmailField(label='Email', widget= forms.EmailInput())
    username = forms.CharField(label='Username', widget=forms.TextInput())
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Retry password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginUser(AuthenticationForm):
    username = forms.CharField(label='Username', widget = forms.TextInput())
    password = forms.CharField(label='Password', widget=forms.PasswordInput())