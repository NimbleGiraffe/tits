from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=100, required=False)
    
    def clean(self):
        username = self.cleaned_data.get('username', None)
        password = self.cleaned_data.get('password', None)
        if username and password:
            try:
                user = User.objects.get(username=self.cleaned_data['username'])
            except:
                self._errors["username"] = self.error_class(["We could not find an account with that username."])
                return
            if user is None or not user.is_active:
                self._errors["username"] = self.error_class(["We could not find an account with that username."])
                return
            if not user.check_password(self.cleaned_data['password']):
                self._errors["password"] = self.error_class(["Password was incorrect."])
                return
            return self.cleaned_data
        else:
            self._errors['username'] = self.error_class(['A valid username and password are required.'])
            return