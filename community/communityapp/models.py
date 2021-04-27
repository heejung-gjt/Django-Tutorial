from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Category(models.Model):
  title = models.CharField(max_length=30)
  date = models.DateField()
  def __str__(self):
    return self.title

class Article(models.Model):
  category = models.ForeignKey(Category, on_delete = CASCADE, related_name = 'article')
  title = models.CharField(max_length=30)
  content = models.TextField()
  date = models.DateField()
  writer = models.CharField(max_length=30)
  def __str__(self):
    return self.title