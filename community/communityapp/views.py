from django.shortcuts import render
from .models import Article, Category
from communityapp import models
# Create your views here.

def index(request):
  category = Category.objects.all()
  context = {
    'categories' : category
  }
  return render(request, 'index.html',context)

def category(request,pk):
  category = Category.objects.filter(pk=pk).first()
  context = {
    'category':category,
  }
  return render(request, 'category.html',context)

def article(request,pk):
  article = Article.objects.filter(pk=pk).first()
  context = {
    'article':article,
  }
  print(article)
  return render(request,'article.html',context)