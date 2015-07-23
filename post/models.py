from django.db import models

class Article(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  likes = models.IntegerField(default=0)

  def __unicode__(self):
    return self.title

class Chatter(models.Model):
  name = models.CharField(max_length=20, default="Anonymous")
  created = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return self.name
