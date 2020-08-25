from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, PreSchedule

class Login(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class Upload(forms.Form):
    file = forms.FileField()

class EditSchedule(forms.ModelForm):
    name = forms.CharField(max_length=30)

    class Meta:
        fields = ['name',]
        model = PreSchedule

class CreateUser(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model= User
        fields = ('email',)
        help_texts= {"password1":None, "password2":None}
