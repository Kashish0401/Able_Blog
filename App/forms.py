from django import forms
from .models import PostModel

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea({'rows':4}))
    class Meta:
        model = PostModel
        fields = ('title', 'content') 