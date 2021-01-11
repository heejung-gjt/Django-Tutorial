## 쇼핑몰 기능 구현하기   

구축 순서 : 프로젝트,앱 생성 -> model 생성 -> DB 생성 -> admin 페이지 수정 -> 

- ### 가상환경 구축하고 django 설치하기   

```bash
$ python -m venv shopping_env
$ source shopping_env/Scripts/activate
$ pip install django
```

<br>

- ### 프로젝트(쇼핑몰)와 3개의 앱(회원, 상품, 주문) 설치하기   

```bash
$ django-admin startproject shopping_django
$ cd shopping_django # 프로젝트 안에서 app 생성하기
$ django-admin startapp user
$ django-admin startapp product
$ django-admin startapp order
```
<br>

- ### model 생성하기   

1. user에 있는 models.py 작성하기    
email, pwd, 등록날짜의 필드를 갖는 User class를 생성한다.   
admin 관리자 페이지에서 보여질 name을 class meta를 이용하여 변경해준다

##### user/models.py

```python
class User(models.Model):
  email = models.EmailField(verbose_name='이메일')
  pwd = models.CharField(max_length=64, verbose_name='비밀번호')
  register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

  def __str__(self):
    return self.email
        
  class Meta:
    db_table = 'user'
    verbose_name = '사용자'
    verbose_name_plural = '사용자'
```
<br>

2. product에 있는 models.py 작성하기    
상품명, 가격, 설명, 재고, 등록날짜의 필드를 갖는 Product class를 생성한다.   
admin 관리자 페이지에서 보여질 name을 class meta를 이용하여 변경해준다    
```def__str__(self) : return self.name``` admin에서 각 model을 문자열로 변환했을때 표시하는 함수를 생성한다 

##### product/models.py

```python
class Product(models.Model):
  name = models.CharField(max_length=256, verbose_name='상품명')
  price = models.IntegerField(verbose_name='상품가격')
  description = models.TextField(verbose_name='상품설명')
  stuck = models.IntegerField(verbose_name='재고')
  register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
  
  def __str__(self):
    return self.name
  
  class Meta:
    db_table = 'product'
    verbose_name = '상품'
    verbose_name_plural = '상품'
```
<br>

3. oreder에 있는 models.py 작성하기    
user, 상품, 재고, 등록날짜의 필드를 갖는 order class를 생성한다. 
admin 관리자 페이지에서 보여질 name을 class meta를 이용하여 변경해준다   
return str(self.user) + ' ' + str(self.product) :

#### [ForeignKey 알아보기 👉click]()

##### order/models.py   

```python
class Order(models.Model):
  user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='사용자')
  product = modles.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')
  quantity = models.IntegerField(verbose_name='수량')
  register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

  def __str__(self):
    return str(self.user) + ' ' + str(self.product)

  class Meta:
    db_table = 'order'
    verbose_name = '주문'
    verbose_name_plural = '주문'
```
<br>

- ### 데이터베이스 생성하기   

❗ migration 하기 전에 settings INSTALLEC_APPS에 생성한 앱들을 등록해주는 것을 잊지말자 

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br>

- ### [admin 관리자 페이지 구성하기 👉click](https://heejung-gjt.github.io/django-02-MTV)

각 앱에 있는 admin.py를 수정해준다   

1. user/admin.py 수정   
models.py에 있는 User class를 import해준다   

```python
from .models import User

class UserAdmin(admin.ModelAdmin):
  list_display=('email',)
admin.site.register(User, UserAdmin)
```
<br>

2. product/admin.py 수정   
models.py에 있는 product class를 import해준다   

```python
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')
admin.site.register(Product, ProductAdmin)
```
<br>

3. order/admin.py 수정   
models.py에 있는 order class를 import해준다   

```python
from .models import Order

class OrderAdmin(admin.ModelAdmin):
  list_display=('user','product')
admin.site.register(Order, OrderAdmin)
```
<br>

```python manage.py createsuperuser```로 관리자 계정을 생성뒤 접속하면 다음과 같이 화면이 나온다    

![관리자](https://user-images.githubusercontent.com/64240637/104196500-3277aa80-5467-11eb-83e0-386c1ddfc251.PNG)

<br>

- ### 각각의 view를 class 이용해서 작성하기   
제너릭 뷰 이용하기


