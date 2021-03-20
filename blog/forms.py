from django.forms import ModelForm
from blog.models import *
from django import forms
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