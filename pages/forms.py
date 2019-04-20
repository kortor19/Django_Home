from django import forms
from .models import Contact
from .models import *
from .models import Post


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'your_email', 'message_body')



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields =['title', 'content']


    
    