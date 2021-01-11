from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password
#폼에서 데이터를 검증할 클래스를 작성하기 때문에 뷰는 굉장히 깔끔해진다.
# 로그인 폼을 만들고 폼이 정상적인지 확인해준다


#장고에 있는 form 사용할 수 있다 . 장고에서 자동으로 생성해준 form 이다
#forms안에 로그인폼을 만든후 해당 form을 가져와서 view에서 클래스 변수를 만든 후 템플릿에 전달함. 그후 템플릿에서 폼을 {{form}} 출력함
class LoginForm(forms.Form): #2개의 필드를 사용하는 폼이 생성됨
    username = forms.CharField(
        error_messages={
            'required':'아이디를 입력해주세요'
        },
        max_length=32, label='사용자이름')
    password = forms.CharField(
        error_messages={
            'required':'비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                fcuser = Fcuser.objects.get(username=username)
            except Fcuser.DoesNotExist:
                self.add_error('username','ID가 없습니다')
                return
            if not check_password(password, fcuser.password):
                self.add_error('password','Password를 틀렸습니다')
            else:
                self.user_id = fcuser.id