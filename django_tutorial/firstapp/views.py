from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#임시 데이터베이스 
students = ['이한결','이영민','김성수','이찬민','최은비','김주형']

def index(request):
  return render(request,'index.html')

def result(request):
  if request.method == 'POST':
    text = request.POST['text']
    textarea = request.POST['textarea']
    context = {'text':text, 'textarea':textarea, 'verify':False}
    if text in students: 
      context['verify'] = True
      context['is_blank_text'] = len(textarea)
      context['no_blank_text'] = len(textarea.replace(' ',''))
  return render(request, 'result.html',context)