## 🗝 Django tutorial (Django structure)


### 목차
   
✔ startproject

✔ startapp
 
 <br>

## [startproject](https://heejung-gjt.github.io/django-01)

### 생성되는 파일들

community 라는 프로젝트(root 앱)를 생성했다고 가정해보자.   

```bash
$ django-admin startproject community
```
<br>

startproject 명령어로 생성된 루트앱 안의 파일들이다   

```bash
community/
  manage.py
   community/
    __init__.py
    settings.py
    urls.py
    asgi.py
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




## [startapp](https://heejung-gjt.github.io/django-01)

### 생성되는 파일들

user 라는 앱을 생성했다고 가정해보자.   

```bash
$ django-admin startapp user
```
<br>

startapp 명령어로 생성된 user앱 안의 파일들이다   

```bash
user/
 __init__.py
 admin.py
 apps.py
 migrations/
  __init__.py
 models.py
 tests.py
 urls.py # 직접 생성
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
 (참고01)[https://livetodaykono.tistory.com/41]   
 (참고02)[https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/skeleton_website]   
 (참고03)[https://velog.io/@ikswary/django-%EA%B5%AC%EC%A1%B0]   
 (참고04)[https://docs.djangoproject.com/ko/3.1/intro/tutorial01/]   
