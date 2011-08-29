from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(), max_length=100, required=False)
    
    def clean(self):
        email = self.cleaned_data.get('email', None)
        password = self.cleaned_data.get('password', None)
        if email and password:
            try:
                user = User.objects.get(email=self.cleaned_data['email'])
            except:
                self._errors["email"] = self.error_class(["We could not find an account with that email address."])
                return
            if user is None or not user.is_active:
                self._errors["email"] = self.error_class(["We could not find an account with that email address."])
                return
            if not user.check_password(self.cleaned_data['password']):
                self._errors["password"] = self.error_class(["Password was incorrect."])
                return
            return self.cleaned_data
        else:
            self._errors['email'] = self.error_class(['A valid email and password are required.'])
            return