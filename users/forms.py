from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    ROLE_OPTIONS = [('user', 'User'), ('contributor', 'Contributor')]
    role = forms.ChoiceField(required=True, choices=ROLE_OPTIONS, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
