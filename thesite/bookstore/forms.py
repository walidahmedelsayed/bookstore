from django import forms

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password','repassword']
        widgets = {
            'password': forms.PasswordInput(),
            'repassword': forms.PasswordInput(),
        }