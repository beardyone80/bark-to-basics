# from .models import Home
from django import forms
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)