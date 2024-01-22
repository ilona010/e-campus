from django.contrib.auth.forms import forms
from django.forms import ModelForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['type', 'description', 'file']
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Опис', 'class': 'form-control', 'rows': '5'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'file': forms.FileInput(),
        }
