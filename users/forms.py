from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # nest namespace for configurations,
    # when we save the form its going to save it to the User model, form fields in order
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Allows the user to update their username and email
class UserUpdatteForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']