from django import forms 
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']

class CommentForm(forms.Form):
    content = forms.CharField(max_length=1000)