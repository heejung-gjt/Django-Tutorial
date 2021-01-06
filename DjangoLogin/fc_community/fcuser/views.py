from django.http import HttpResponse  #장고 오류 메시지 http에 뜨게
from django.contrib.auth.hashers import make_password, check_password # admin에서 pwd 암호화되서 보이게 해준다
#비밀번호를 비교하는 함수 = check_password
from django.shortcuts import render, redirect
from .models import Fcuser

# Create your views here.

def login(request):  #template인 login.html과 연결시켜준다
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        pass

        return render(request, 'login.html')
