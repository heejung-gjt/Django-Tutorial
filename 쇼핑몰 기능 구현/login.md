### 📌FormView를 사용한 로그인 기능 구현하기  

- ### view를 생성하자   

##### user/views.py

```python
from .forms import RegisterForm, LoginForm  #LoginForm 아직 생성 x

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'
```
<br>

- ### login.html 생성하자   
login.html 파일은 [register.html]()과 동일하게 생성하면 된다. "로그인"으로만 변경해주자   
<br>

- ### forms.py에서 LoginForm을 생성하자    

##### user/forms.py
```python
class LoginForm(forms.Form): 
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

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)

            except User.DoesNotExist:
                self.add_error('email','이메일이 없습니다')
                return
            
            if not check_password(password, user.password): #비밀번호 암호화
                self.add_error('password','비밀번호를 틀렸습니다')
            else:
                self.email = user.email
```
<br>

- ### 3에서 form에 대한 유효성 검사가 끝났다. 이제 login session을 추가해주자   

##### user/views.py

```python
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self,form):  #session 추가
        self.request.session['user'] = form.data.get('email')

        return super().form_valid(form)

```
<br>

- ### url 연결을 해주자   

##### shopping_djnago/shopping_django

```python
from user.views import index, RegisterView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
]

```
<br>

- ### index.html에서 login 한 email을 출력한다   index.html에 {{email}}추가하고 views.py에서 session
안에 있는 user를 가져온다

```python
def index(request):
    return render(request,'index.html',{'email':request.session.get('user')})

```