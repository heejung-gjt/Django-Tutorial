from django.shortcuts import render,redirect
from .models import Article, Category
from communityapp import models
import datetime
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
  return render(request,'article.html',context)

def add_category(request):
  if request.method == 'POST':
    title = request.POST.get('text')
    category = Category(
      title = title,
      date = datetime.date.today()
    )
    category.save()
    return redirect('/')
  return render(request, 'add_category.html')

def write(request):
  if request.method == 'POST':
      title = request.POST.get('text')
      content = request.POST.get('textarea')
      writer = request.POST.get('writer')
      article = Article(
        title = title,
        content = content,
        date = datetime.date.today(),
        writer = writer,
      )
      article.save()
      return redirect('article/')
  return render(request, 'write.html')
