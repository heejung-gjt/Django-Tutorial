# 🗝 Django tutorial (What is Django ?)

## 목차
    
✔ Installation

✔ MTV code pattern
   
✔ startproject

✔ startapp
   
<br>
    
## Installation

### 가상환경 세팅하기

패키지 간의 버전차이, 여러 충돌을 방지하기 위해 가상환경을 구축한다.
가상환경이 성공적으로 설정되면 터미널안에 venv가 생성된다.(보통 가상환경 네이밍은 venv로 지정)
생성된 가상환경에서 django를 설치한다.
 

```bash
$ virtualenv venv # venv가상환경 설정
$ source venv/bin/activate  # 가상환경 실행
$ pip install django # 원하는 패키지 설치 
```

### 프로젝트 생성

django 프로젝트는 하나의 프로젝트와 여러개의 app으로 구성된다. app안에는 model, view, template, url매핑등 여러가지 app들로 나누어서 구성하고 있다. app들을 여러개로 구성함으로써 개발 및 유지 보수를 효율적으로 할 수 있는 장점이 있다.    

```예를 들자면 project는 네이버 전체이며 app들은 네이버에서의 기능들, 로그인 기능, 메일기능, 댓글기능들을 말한다```

<br>

__django-admin__ 명령어를 통해서 프로젝트와 app을 생성한다. 생성된 app안에 templates 폴더를 만들어준다.
Template은 html 파일로서 장고 app 폴더안에 생성하는데 요청된 정보들을 화면에 보여주기 위해 사용되는 파일이다    

이때 프로젝트 생성시 뒤에 .을 꼭 붙여주자 ! 아니면 폴더안에 폴더가 생성되는 구조로 만들어진다 

```bash
$ django-admin startproject firstproject .#firstproject 프로젝트 생성
$ django-admin startapp firstapp  # firstapp 앱 생성
```

### 프로젝트 실행

만들어진 프로젝트를 runserver를 통해서 실행해준다. 이때 manage.py 파일이 있는 경로에서 실행해야 한다

```bash
$ python manage.py runserver
```
![runserver](https://user-images.githubusercontent.com/64240637/103471082-c2aa5580-4dbe-11eb-8a15-48de2b48b445.PNG)

위의 화면이 뜨면 제대로 install 된것 🙌   
<br>

## MTV code pattern

### MTV 생성

django에서 MTV 패턴은 프로젝트 내에서 유저의 요청부터 응답까지 동작하는 방식에 대한 패턴이다. 
생성된 app 안에는 model과 view는 생성이 되어져있다. template을 사용자가 따로 생성해야 하는데 보통 앱안에서 생성을 한다.

- __Model__ 은 DB에 저장되는 데이터를 의미한다. models.py에서 생성되는 클래스는 DB의 구조로 생성되어진다. 데이터를 처리하는 로직을 가지고 있다   

- __Template__ 은 사용자에게 보여지는 부분이다. 사용자가 직접 접근하는 html 등과 같은 페이지를 구성한다.    

- __View__ 는 template에서 받은 request을 처리하고 받은 데이터를 로직으로 가공하여 response 해주는 역할을 한다. 


#### 1.Model 생성 (  firstapp 안에 있는 MTV )

📌  __django의 models.py 로직을 생성__   

```bash
$ class User(models.Model):
    username = models.CharField(max_length=32,verbose_name='사용자명')
    password = models.CharField(max_length=64,verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,verbose_name='등록시간')
    class Meta:
        db_table = 'campus_user'
   
```
<br>

📌 __프로젝트에 생성되어져 있는 manage.py 를 통해 model에서 만들어진 로직으로 DB생성__   

```bash
$ python manage.py makemigratons
$ python manage.py migrate   #table 생성
```
📝 이때 생성한 프로젝트 내에 있는 settings.py 에서 INSTALLED_APPS 안에 user app을 넣어주어야 db가 생성된다.   

<br>

📌 __프로젝트내 db.sqlite3이 생성. 해당 db를 확인하기 위해서 [db browser for sqlite](https://sqlitebrowser.org/dl/)
다운받아 확인__   
<br>
데이터베이스 열기에서 db.sqlite3 선택, 해당 db를 변경시 manage.py 명령어로 실행시키면 업데이트된 db를 확인할 수 있다.

- 아래 명령어를 통해서도 확인 할 수 있음 (sqlite3 실행 안됨 , db browser for sqlite로 확인 가능)
```bash
$ sqlite3 db.sqlite3
sqlite> .tables
```

<br>

#### 2.Templates 생성

📌 __Templates 폴더에서 home.html 파일등 화면에 필요한 html등을 작성한다__

[bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)을 통해서 html, css를 가져올 수 있다.
Template은 view에 request하고 response를 받아온다.   

form에서 Data를 request 하는데 두가지의 방식이 있다   
- method="POST"
- method="GET"   
데이터를 request 받은 view는 로직으로 가공하여 template에 response 한다.

<br>

#### 3.View 생성

📌 __views.py 에서 template에서 요청받은 데이터를 논리적으로 가공하여 반환해준다.   
   이때 view에서는 요청받은 데이터를 실행, 수정, 삭제등을 할 수 있다.__

```ython
def register(request):
    if request.method =='GET':
        return render(request, 'register.html')
    elif request.method =='POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
    return render(request, 'register.html', res_data)
```

<br>

* * *

## startproject

### 생성되는 파일들

firstproject 라는 프로젝트(root 앱)를 생성했다고 가정해보자.   

```bash
$ django-admin startproject firstproject
```
<br>

startproject 명령어로 생성된 루트앱 안의 파일들이다   

```bash
firstproject/
  __init__.py
  asgi.py
  settings.py
  urls.py
  wsgi.py
```
<br>

### 📌settings.py   
현재 django 프로젝트의 모든 환경과 구성을 포함하고 있으며 저장한다. 앞으로 생성되어지는  해당 파일에는 사용자가 만드는 모든 app, 정적 파일 위치,DB 설정 등을 등록한다.   
- __INSTALLED_APPS__ 프로젝트에서 생성한 모든 앱들을 명시해주어야 한다. 앱들의 모든 경로가 위치하는 영역이다.    

- __DATABASES__ DB를 사용하기 위한 영역이다. 기본값으로 sqlite이 지정되어 있다.      

-  __STATIC_DIRS__ 정적 파일들의 경로를 설정하는 영역이다.

<br>

```python
from pathlib import Path
import os
.
.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'community',  # 생성한 (root앱) 명시

]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/' 
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'), ]
.
.
```
<br>

### 📌urls.py   
startapp 명령어로 생성된 앱안에 기본으로 들어있는 파일이다. 사이트의 url과 뷰의 연결을 지정해주고 메인 프로젝트 (root 앱)에서 include하여 넘겨주는 역할을 한다.

<br>

#### root앱 프로젝트 생성시 만들어진 urls.py

- 프로젝트 community(root앱)을 생성했을때 자동으로 생성된 urls.py이다. include는 찾은 url 패턴을 다른 urls 파일로 넘겨주는 역할을 한다.   
즉 url에 user/ 라는 단어가 있는 경우 include를 통해서 생성한 user앱의 urls파일로 넘겨준다. user/ 에 대한 내용을 찾아 user.urls파일에서 처리해준다

```python
from django.contrib import admin
from django.urls import include,path
from fcuser.views import home


urlpatterns = [
    path('user/', include('user.urls')),
]

```
<br>

### 📌manage.py 
manage.py는 어플리케이션을 생성하고 DB와 작업하고 웹 서버를 시작하기 위해 사용된다. command창에서 사용되는 명령어이다.   

```bash
django-admin startproject <name> # 새로운 <name> 프로젝트를 생성
python manage.py <name> # 새로운 <name> 프로젝트를 생성
python manage.py makemigrations <name> : 마이그레이션 파일 생성
python manage.py migrate <name> : 마이그레이션 적용
# migrate, makemigrations 명령어는 models.py에 정의된 모델의 생성과 변경 내역을 히스토리 관리, db에 적용 등의 기능을 제공한다.

python manage.py runserver # 개발 서버 실행

```
<br>

## startapp

### 생성되는 파일들

user 라는 앱을 생성했다고 가정해보자.   

```bash
$ django-admin startapp user
```
<br>

startapp 명령어로 생성된 user앱 안의 파일들이다   

```bash
firstapp/
migrations/
__init__.py
admin.py
apps.py
models.py
tests.py
views.py
```
<br>

### 📌urls.py
#### user app 생성시 만들어진 urls.py

- app 을 생성했을때 자동으로 생성된 urls.py이다. 이전에 community urls.py에서 user/로 들어오는 url을 include를 사용하여 user urls.py에 넘겨주었다. user의 url을 살펴보면 register/뒤에 무엇이 오는지를 보고 처리해준다. 예를 들어 user/login, user/logout이 주소에 오는 경우 urlpatterns에서 각각의 login과 logout이라는 패턴을 순타적으로 탐색한다. 그 뒤 import한 views 함수를 이용해서 어떤 화면을 보여줄 것인지 정한다. urls.py의 역할은 여기까지 이다. 


```python
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),  # login/으로 들어오는 url 연결해준다
    path('logout',views.logout)
]

```
<br>

#### 그럼 template를 생성하기 전 HttpResponse만으로 화면에 무언가를 출력해보자      

일단, urls.py에서 root에서 실행될 데이터를 가지고 있는 views를 import해준다.
이때 name을 지정해주는 이유는 template에서 요청을 위해 접근할때가 있는데 그때 name이 기준이 된다. 하지만 지금은 단순히 response로 접근하기 때문에 필요하지는 않다.    
```python
# html에서 접근되는 방식
{% url 'index' %}
```  
```python
# urls.py

from firstapp import views

urlpatterns = [
    path('', views.index, name = "index"),
]
```
그 후 views.py에서 index 함수를 만들어 응답을 리턴해준다   
```python
# views.py

def index(request):
    return HttpResponse('출력 성공!')
```
화면에 ```출력 성공```이 뜨면 성공한 것 !    

<br>

#### 이제 template폴더를 만들고 views에서 index.html을 render해보자     

templates 폴더를 app안에 생성해주자. 그리고나서 index.html파일을 만든다. 그 후 html을 작성해준다(template에 s 붙여주는거 잊지말자!)
```html
<!DOCTYPE html>
<html lang="en">
<head>
<title>tutorial - 02</title> 
</head>
<body>
  <h1>출력 성공 !</h1>
</body>
</html>
```

이미 urls.py에서는 index를 연결해주었기 때문에 views에서 index로 render해주면 된다. 화면에 ```출력 성공 !```이 뜨면 제대로 응답이 된 것이다
```python
# views.py
from django.shortcuts import render

def index(request):
  return render(request,'index.html')

```

<br>

#### 이제 result.html을 만들고 index.html에서 폼을 작성해 button을 누르면 result.html로 이동하는 것을 해보자    

먼저 result.html을 똑같이 만들어 준 후 urls.py로 연결해준다.
```python
# urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
]
```
views.py에서 해당되는 result함수를 작성해준다. 이후 생성한 result.html을 render해주면 된다  
```python
# views.py

def result(request):
  return render(request, 'result.html')
```

index.html에 form태그를 작성한다. method로 데이터를  요청하게 되는데 POST이므로 데이터를 action에 적혀있는 result로 보낸다. 여기서 쓰인 result가 urls에 적었던 name과 동일해야 한다.     
```html
 <form action="{% url 'result' %}" method="POST">
    {% csrf_token %}
    <button type="submit">결과 페이지로 이동하기</button>
```
이제 해당 버튼을 누르면 result.html이 렌더링되어 화면에 보여지게 된다 

<br>

#### 이제 작성한 form에 input받아 작성한 데이터를 result.html에서 출력될 수 있게 해보자. 해당 데이터를 views에서 가져와 쓸 수 있게 input에는 name을 작성해야 한다
```html
<input type="text" name="text">
```
views에서 요청을 받은 데이터를 가장 먼저 POST방식인지 아닌지를 판단해준 후 요청받은 데이터를 ```request.POST['text]```로 가져온다     
이때 데이터를 원하는 방식으로 가공할 수 있다. 지금은 간단하게 받은 데이터를 result.html에서 출력할 수 있게 context라는 딕셔너리에 데이터를 넣어준다.
```python
def result(request):
  if request.method == 'POST':
    text = request.POST['text']
    context = {
      'text' : text
    }
  return render(request, 'result.html',context)
```
이후 result.html에 원하는 형식으로 데이터를 출력할 수 있게 작성해준다
```html
<!-- result.html -->
  <h1>여긴 결과 페이지입니다</h1>
  <h2>입력한 텍스트는 {{ text }} 입니다</h2>
```

이제 우리가 index.html에서 input으로 작성한 텍스트는 result에서 볼 수 있다

#### 그렇다면 이제 마지막으로 views에서 데이터를 원하는 정보롤 가공하여 화면에 그려주자

views에 임시로 데이터베이스 데이터를 만들고 text에서 작성한 데이터와 같으면 textarea에 작성한 텍스트들을 카운트 해주어 result.html에 출력해준다. 만약 같지 않으면 같지 않다는 에러 메세지를 출력해준다      

__1. index.html에 textarea을 추가해준다. 이때 name을 작성하는 것 잊지말자 !__   
```html
<!-- index.html -->
<input type="text" name="text"><br/><br/>
<textarea name="textarea"></textarea><br/>
<button type="submit">결과 페이지로 이동하기</button>
``` 

__2. views에 임시 데이터를 작성한다__
```python
#views.py
students = ['이한결','이영민','김성수','이찬민','최은비','김주형']
```

__3. form에서 데이터를 받는 result에서 로직을 작성한다__    
가장 먼저 index.html에서 보낸 데이터를 변수에 넣어준 후 딕셔너리 형태로 가공해준다. 이후에 input에 받은 데이터가 데이터베이스(students라고 부르자)안에 있는지부터 알아본다. 만약 데이터가 없으면 context를 알맞게 수정해준다  
```python
def result(request):
  if request.method == 'POST':
    text = request.POST['text']
    textarea = request.POST['textarea']
    context = {'text':text, 'textarea':textarea, 'verify':False}
    if text in students: context['verify'] = True
  return render(request, 'result.html',context)
```
여기서 verify의 역할은 result.html에서 조건문을 걸기 위해 필요한 값이다   

```html
<!-- result.html -->
<h1>여긴 결과 페이지입니다</h1>
{% if verify %}
<h3>{{ text }}님 접속 성공 !</h3>
{% else %}
<h3>{{ text }}님 접속 실패</h3>
{% endif %}
```

이제 진짜 진짜 마지막으로 접속에 성공했을때 Textarea에 작성했던 텍스트들을 카운트해준다. 이때 공백포함/공백미포함 개수를 함께 카운트해준다. 이를 위해서는 views.py에서 이에 맞게 데이터를 가공해준다
```python
#views.py
context = {'text':text, 'textarea':textarea, 'verify':False}
if text in students: 
    context['verify'] = True
    context['is_blank_text'] = len(textarea)
    context['no_blank_text'] = len(textarea.replace(' ',''))
```

이제 result.html에 보여주고 싶은대로 작성해주면 된다. 이때 html에서 장고 템플릿 문법을 사용하여 조건을 걸어준다. __화면 가독성을 위해서 h태그를 사용하였다__
```html
<h1>여긴 결과 페이지입니다</h1>
  {% if verify %}
  <h3>{{ text }}님 접속 성공 !</h3>
  <br>
  <div>
    <h4>{{ textarea }}</h4>
    <h4>공백 포함한 총 개수 : {{ is_blank_text }}</h4>
    <h4>공백 미포함 총 개수 : {{ no_blank_text }}</h4>
  </div>
  {% else %}
  <h3>{{ text }}님 접속 실패</h3>
  {% endif %}
```
장고 문법으로 {% if %} ~ {% else %} ~{% endif %}을 사용하였다. 이는 앞으로 차차 알아볼 예정이므로 이렇게 넘어가도록 하자. 데이터에서 받은 bool형 데이터로 이름이 데이터베이스에 존재할 경우와 존재하지 않는 경우를 나누어 화면에 그려준다    

![SITE](https://user-images.githubusercontent.com/64240637/115553660-a3d9bb80-a2e8-11eb-925f-80019d469bde.png)
![SITE2](https://user-images.githubusercontent.com/64240637/115553664-a50ae880-a2e8-11eb-8276-559bccd452b6.png)

<br>

#### 이제 간단한 실습을 통해서 기본적으로 장고가 어떤식으로 돌아갔는지 알게 되었다. :-)