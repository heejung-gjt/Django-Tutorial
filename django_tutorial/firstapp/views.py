from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
  return render(request,'index.html')

def result(request):
  if request.method == 'POST':
    text = request.POST['text']
    context = {
      'text' : text
    }
  return render(request, 'result.html',context)