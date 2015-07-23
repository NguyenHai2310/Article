from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView, FormView
from .models import Article
from .forms import ChatterForm, ArticleForm

class Home(FormView):
  template_name = "home.html"
  form_class = ChatterForm
  success_url = "/articles/index"

class ArticleIndex(ListView):
  model = Article
  context_object_name = "articles"
  template_name = "index.html"
  paginate_by = 5

class Article(DetailView):
  model = Article
  template_name = "article.html"

class CreateArticle(FormView):
  template_name = "create_article.html"
  form_class = ArticleForm
  success_url = "/articles/index"
