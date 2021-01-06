## 🗝 Django tutorial (로그인 페이지 연결)


### 목차

✔ static 설정

✔ MTV 생성

 

## static 설정
root 앱에 static 폴더를 생성한다.    
생성한 static 폴더는 settings.py에 있는 STATICFILES_DIRS로 연결해준다   
```python
import os

STATIC_URL = '/static/'
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'), ]
```
<br>

html head에 static 파일 css를 사용할 수 있도록 설정해준다
```html
<head>
    {% load static %}
    <link rel="stylesheet" href="{% static 'login.css' %}" />
</head>
```

## MTV 생성

### 📌 (Template) 생성
login 화면을 구현할 html 을 templates에 넣어야 한다.   

__HTML 작성시 주의할점__  
- 받는 method가 POST인지 GET인지 설정해주자
- form 작성시 보안을 위한 {% csrf_token %} 을 잊지말자

<br>

### 📌 (View) Templates인 login.html의 화면이 정상적으로 출력될 수 있게 views.py에서 해당 template과 연결해준다.   
- GET 방식은 클라이언트의 데이터를 URL에 붙여서 보낸다. URL에 /user/login 을 작성해서 request 하는 방식이다.   
- POST 방식은 데이터 전송을 기반으로 한 요청 메소드이다. 이 방식은 HTML body에 데이터를 넣어서 보내게 된다.

view에서는 login.html을 렌더링한다. 이때 __렌더링이란 html코드를 view에서 해석하여 웹 화면에 보여준다고 생각하면 된다.__

```python
from django.http import HttpResponse
from django.shortcuts import render 

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method =='POST':
        pass
        return render(request, 'login.html')
```
<br>

### 📌 (urls) 만들어진 view를 화면에 보여주기 위해서 urls.py에 설정해준다   
 login/으로 들어오는 url 연결해준다

```python
from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login), 
]
```