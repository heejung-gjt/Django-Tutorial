### 📌회원가입 기능 구현하기  

구축 순서 : view에서 index.html로  -> base.html 만들기 -> 회원가입 후 첫페이지로 이동할 수 있는 index.html 만들기 ->    

- ### views.py에 index.html 보여주기
 
 ##### user/views.py   
 
 ```python
 def index(request):
  return render(request, 'index.html')
 ```
 
 <br>
 
 - ### templates 폴더에 base.html 과 index.html 생성하기    
 
 (html은 bootstrap을 기반으로 생성하였다)     
 index.html은 웹의 home이 될 예정이다    
 
 
 ##### user/templates/base.html  
 
 ```base.html
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <title>Document</title>
</head>
<body>
    <div class="container">
        {% block contents %}
        {% endblock %}
    </div>    
</body>
</html>
 ```
<br>

##### user/templates/index.html   

 ```index.html
{% extends "base.html" %}

{% block contents %}
hello world
{% endblock %}
 ```
<br>

- ### index.html url 연결해주기   

##### shopping_django/shopping_django/urls.py

```python
from django.urls import path
from user.views import index

urlpatterns = [
  path('', index),
]
```
<br>   

- ###  user/forms.py 생성하기 (회원가입 form)
회원가입 폼을 생성해준다. 회원가입 할 때 입력받는 값을 작성한다

##### user/forms.py

```python
from django import forms

class RegisterForm(forms.Form): # 회원가입 폼 생성
    # 회원가입 할때 입력받는 값
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required':'비밀번호를 입력해주세요'
        },
        widget = forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required':'비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )
```
<br>  

- ### formview 가져와서 views.py 작성하기   

forms.py에서 값들을 입력받고 해당 값들이 유효한 값인지 모두 작성했는지등의 검사를 하기 위한 기능을 view에서 해준다   
이때 더욱 편리하고 간단하게 기능을 구현하기 위해 django 클래스에 있는 FormView를 이용해준다   
register.html도 user/templates에 만들어주자

##### user/views.py

```python
from djagno.views.generic.edit import FormView
from .forms import RegisterForm

class RegisterView(FormView):   //화면은 registe.html을 보여주고 사용되는 form은 RegisterForm이다. 만약 검증후 틀린내용이 없다면 success_url로 home화면으로 돌아갈 수 있다
  template_name = 'register.html'  
  form_class = RegisterForm
  success_url = '/'
```
<br>

- ### register.html url 연결해주기   
class를 연결해주는 경우 as_view() 함수를 사용해야한다. register/ 화면이 잘 나오면 template연결을 성공한 것 !   

##### shopping_django/shopping_django/urls.py

```python
from django.urls import path
from user.views import index, RegisterView

urlpatterns = [
  path('register/',RegisterView.as_view()),
]
```

<br>   

- ### 작성한 RegisterForm 사용하기   
register.html에서 form을 사용해보자

##### register.html
```
{% extends "base.html" %}

{% block contents %}
this is register page {{ form }}
{% endblock %}
```
<br>
회원가입 폼(RegisterForm)이 출력이 되는 것을 볼 수 있다   
<br>

![form](https://user-images.githubusercontent.com/64240637/104416906-e7b97800-55b7-11eb-8bdd-5ce7116b315b.PNG)

<br>

- ### register.html bootstrap이용해서 화면을 수정 한 후 form 출력하기   

##### user/register.html

```html
{% extends "base.html" %}

{% block contents %}
    <div class="row mt-5">
        <div class="col-12 text-center">
            <h1>회원가입</h1>
        </div>
    </div>
    <div class="row mt-5">
        <div class="col-12">
            {{error}}
        </div>
    </div>
    <div class="row mt-5">
        <div class="col-12">
            <form method="POST" action=".">
                {% csrf_token %}
                {% for field in form %}
                <div class="form-group">
                    <label for="{{ field.id_for_label }}">{{ field.label }}</label>
                    {{field.field.widget.name}}
                    <input type="{{ field.field.widget.input_type }}" class="form-control" id='{{                                     field.id_for_label }}' placeholder="{{ field.label }}"name='{{ field.name }}'>
                </div>
                {% if field.errors %}
                <span style="color:tomato">{{ field.errors }}</span>
                {% endif %}

                {% endfor %}

                <button type="submit" class="btn btn-primary">회원가입하기</button>
            </form>
        </div>
    </div>
{% endblock %}
```
<br>

![회원가입 form](https://user-images.githubusercontent.com/64240637/104418463-47188780-55ba-11eb-9e5d-77573d0383f9.PNG)

<br>

- ### form에서 값 유효성 검증을 해주는 코드를 작성한다   
RegisterForm 클래스 안에 작성해준다

##### user.py/forms.py

```python
def clean(self):
  cleaned_data = super().clean()
  email = cleaned_data.get('email')
  password = cleaned_data.get('password')
  re_password = cleaned_data.get('re_password')

  if re_password and password:
      if password != re_password:
          self.add_error('re_password','비밀번호가 서로 다릅니다')
      else:  # 만약 두개의 pwd의 값이 같다면 email,pwd값을 model user에 저장해준다 
          user = User(
              email = email,
              pwd = password  #user/models.py에서 패스워드의 변수명이 pwd이다
          )        
          user.save()    

```
<br>

![다름](https://user-images.githubusercontent.com/64240637/104419775-4aad0e00-55bc-11eb-9903-7297f2fe7121.PNG)

<br>