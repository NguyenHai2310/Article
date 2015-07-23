from django.conf.urls import url
from post import views

urlpatterns = [
  url(r'^$', views.Home.as_view(), name="home"),
  url(r'^index/$', views.ArticleIndex.as_view(), name="index"),
  url(r'^get/(?P<pk>\d+)/$', views.Article.as_view(), name="article"),
  url(r'^create/$', views.CreateArticle.as_view(), name="create_article"),
]
