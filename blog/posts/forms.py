from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['text','image']
        
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter post content'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
