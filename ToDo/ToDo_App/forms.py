from django import forms
from django.contrib.auth.models import User
from ToDo_App.models import Task_model


class Register_form(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"})
        }

class login_form(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class Task_form(forms.ModelForm):
    class Meta:
        model = Task_model
        fields = ['name']

        
