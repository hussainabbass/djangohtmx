from django import forms
# from django.contrib.auth.models import User
#
from htmx.models import Login
#
#
class LoginForm(forms.ModelForm):

    class Meta:
     model = Login
     fields='__all__'
