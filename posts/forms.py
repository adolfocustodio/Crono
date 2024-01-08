from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc', 'file', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'})
        }
