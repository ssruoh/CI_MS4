from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'description', 'article_body', 'image')
        exclude = ('author',)

        widgets = {
            'article_body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write an article here!', 'rows': '6'}),
            'image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert a URL link to your image here.', 'rows': '1'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This description will be shown on the Articles page.', 'rows': '1'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'The title of your article.', 'rows': '1'}),
        }
