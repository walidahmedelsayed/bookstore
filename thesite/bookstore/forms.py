from django import forms

from .models import User

from django.contrib.auth.hashers import make_password


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

        widgets = {
            'password': forms.PasswordInput(),

        }

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        user.password = make_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user


class LoginForm(forms.Form):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True,widget=forms.PasswordInput)
