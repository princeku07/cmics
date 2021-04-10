from django.forms import ModelForm
from blog.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = forumcomment
        fields = ('name','body','image')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = commentblog
        fields = ('name','body')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class': 'form-control'}),
            
        }
    
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']