from django import forms
from .models import Article, Comment

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=30)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'


class CommentFormForm(forms.ModelForm):
    
    class Meta:
        model = CommentForm
        fields = '__all__'
