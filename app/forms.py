from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):   
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)    
    
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'password1', 'password2')

class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['created', 'title', 'content', 'due_date', 'category']

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',]
