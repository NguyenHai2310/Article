from django import forms
from .models import Chatter, Article

class ChatterForm(forms.ModelForm):
  class Meta:
    model = Chatter
    fields = ["name"]

class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = ["title", "body", "likes"]
