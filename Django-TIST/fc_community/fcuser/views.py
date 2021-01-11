from django.http import HttpResponse  #장고 오류 메시지 http에 뜨게
from django.contrib.auth.hashers import make_password, check_password # admin에서 pwd 암호화되서 보이게 해준다
#비밀번호를 비교하는 함수 = check_password
from django.shortcuts import render, redirect
from .models import Fcuser
from .forms import LoginForm   #forms.py에 있는 class LoginForm 가지고 옴

# Create your views here.


def home(request):
#세션에 대한 유무확인을 하는 코드였지만 home.html에서 할 수 있으므로 지워준다
  #user_id = request.session.get('user')
    # if user_id: #만약 user가 있으면
    #     fcuser = Fcuser.objects.get(pk=user_id) #기본키를 user_id, 즉 model안에서 id를 pk로 지정해 가져온다
        
    return render(request, 'home.html')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


def login(request):  #template인 login.html과 연결시켜준다
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
        return redirect('/')
    else:
        form = LoginForm()

    return render(request,'login.html', {'form' : form })
    # if request.method == 'GET':
    #     return render(request, 'login.html')
    # elif request.method == 'POST':
    #     username = request.POST.get('username',None)
    #     password = request.POST.get('password',None)

    #     res_data={}
    #     if not (username and password):
    #         res_data['error'] = '모든 값을 입력해야합니다'
    #     else: #데이터베이스가 저장되어 있는 MODEL (Fcuser)를 가져온다
    #         fcuser = Fcuser.objects.get(username=username) #앞의 username은 필드명
    #         if check_password(password, fcuser.password):
    #             #비밀번호 일치할 경우
    #             request.session['user'] = fcuser.id
    #             return redirect('/') #2. 로그인 후 홈으로 이동 == 리다이렉트  /을 작성하면 현재 구현중인 사이트의 root로 이동함
    #             #1. 세션
    #         else:
    #             #비밀번호 오류일 경우
    #             res_data['error']='비밀번호가 틀렸습니다'
        # return render(request, 'login.html', res_data)


def register(request):  #template인 register.html과 연결시켜준다
    if request.method =='GET':
        return render(request, 'register.html')
    elif request.method =='POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data={}

        if not(username and useremail and password and re_password):  #빈문자열도 거짓이기때문에 error
            res_data['error'] ='모든 값을 입력해야 합니다.'
        if password != re_password:
            res_data['error'] ='비밀번호가 다릅니다.'
        else:
            fcuser=Fcuser(
                username = username,
                useremail = useremail,
                password = make_password(password)
            )

            fcuser.save()
        return render(request, 'register.html', res_data)