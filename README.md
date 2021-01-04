## 🗝 Django tutorial (What is Django ?)


### 목차
   
✔ Installation

✔ MTV code pattern
   
✔ Practice
   
<br><br>

## [Installation](https://heejung-gjt.github.io/django-01)

### 가상환경 세팅하기

가상환경 세팅 전에 python 3.x 버전을 설치하여 환경변수에 등록해준다 ( 설치시 Add Python 3.x to PATH 클릭 )

패키지 간의 버전차이, 여러 충돌을 방지하기 위해 가상환경을 구축한다.
가상환경이 성공적으로 설정되면 터미널안에 (venv_django) 가 생성된다.
생성된 가상환경에서 django를 설치한다.
 

```bash
$ python -m venv venv_django   #venv_djanog 가상환경 설정
$ source venv_django/Scripts/activate  # 가상환경 실행
$ pip install django
```

### 프로젝트 생성

django 프로젝트는 하나의 프로젝트와 여러개의 app으로 구성된다. app안에는 model, view, template, url매핑등 여러가지 app들로 나누어서 구성하고 있다. app들을 여러개로 구성함으로써 개발 및 유지 보수를 효율적으로 할 수 있는 장점이 있다.   
<br>
django-admin 명령어를 통해서 프로젝트와 app을 생성한다. 생성된 app안에 templates 폴더를 만들어준다.

```bash
$ django-admin startproject community #community 프로젝트 생성
$ django-admin startapp user  #user 앱 생성
```

### 프로젝트 실행

만들어진 프로젝트를 runserver를 통해서 실행해준다.

```bash
$ python manage.py runserver
```
![runserver](https://user-images.githubusercontent.com/64240637/103471082-c2aa5580-4dbe-11eb-8a15-48de2b48b445.PNG)

위의 화면이 뜨면 제대로 install 된것 🙌
<br>

## [MTV code pattern](https://heejung-gjt.github.io/django-02)

### MTV 생성

django에서 MTV 패턴은 프로젝트 내에서 유저의 요청부터 응답까지 동작하는 방식에 대한 패턴이다. 
생성된 app 안에는 model과 view는 생성이 되어져 있다. template을 사용자가 따로 생성해야 하는데 보통 앱안에서 생성을 한다.

- Model 은 DB에 저장되는 데이터를 의미한다. models.py에서 생성되는 클래스는 DB의 구조로 생성되어진다. 데이터를 처리하는 로직을 가지고 있다   
- Template 은 사용자에게 보여지는 부분이다. 사용자가 직접 접근하는 html 등과 같은 페이지를 구성한다.   
- View 는 template에서 받은 request을 처리하고 받은 데이터를 로직으로 가공하여 reponse 해주는 역할을 한다. 


#### 1.Model 생성 ( user app 안에 있는 MTV )

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

~~~python
def register(request):
    if request.method =='GET':
        return render(request, 'register.html')
    elif request.method =='POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
    return render(request, 'register.html', res_data)
~~~

<br>

## Practice - admin 페이지 

📌 [블로그 참고](https://heejung-gjt.github.io/django-02)
