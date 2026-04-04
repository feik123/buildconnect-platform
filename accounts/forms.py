from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    is_contractor = forms.BooleanField(
        required=False,
        label='Register as contractor'
    )

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2', 'is_contractor')