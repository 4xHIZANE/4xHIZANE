from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from . import models
from django.contrib.auth.models import User
from .models import Comments

class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment_text',)  # Faqat comment_text maydoni qoldiriladi

        widgets = {
            'comment_text': forms.Textarea(attrs={
                'class': 'w-full p-2 rounded bg-gray-700 text-white', 
                'rows': 3, 
                'placeholder': 'Izohingizni yozing...'
            }),
        }
