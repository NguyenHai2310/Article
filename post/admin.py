from django.contrib import admin
from .models import Article, Chatter


class ArticleAdmin(admin.ModelAdmin):
  list_display = ["__unicode__", "created", "likes"]

class ChatterAdmin(admin.ModelAdmin):
  list_display = ["__unicode__"]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Chatter, ChatterAdmin)
