from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    # UserRegustrationForm extends UserCreationForm
    email = forms.EmailField()
    
    class Meta:
        # interacts with the user model
        model= User
        fields = ['username','email','password1','password2']