from django import forms
from ckeditor.fields import RichTextFormField
from .models import Article

class KeywordForm(forms.Form):
    keyword = forms.CharField(max_length=255)

class ArticleForm(forms.ModelForm):
    body = RichTextFormField()
    
    class Meta:
        model = Article
        fields = ['title', 'body']