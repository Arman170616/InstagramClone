from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Email Address'}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Username '}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
