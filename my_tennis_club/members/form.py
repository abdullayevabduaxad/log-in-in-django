from django import forms
from .models import Homework_Login


class Home_Login_Forms(forms.ModelForm):
    class Meta:
        model = Homework_Login
        fields = "__all__"
