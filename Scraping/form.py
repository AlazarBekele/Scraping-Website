from django import forms
from .models import Post

class Post_Input (forms.ModelForm):
    class Meta:

        model = Post
        fields = '__all__'

        widgets = {

            'Title' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'Bio' : forms.Textarea(attrs={
                'class' : 'form-control'
            }),
            'Image' : forms.ClearableFileInput(attrs={
                'class' : 'form-control',
                'type' : 'file'
            })

        }