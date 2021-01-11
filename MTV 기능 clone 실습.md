## ⚡ Django 기초 웹 돌아가는 원리 익히기

<br>

![127 0 0 1_8000-개인-Microsoft_-Edge-2021-01-11-18-53-31_Trim](https://user-images.githubusercontent.com/64240637/104166950-e9abfb80-543e-11eb-8cef-cbf12a6262c0.gif)

<br>

### home, register, login, board 연결하기   


📌home.html 작성하기 (bootstrap이용)   

{% if %} ~ {% endif %} 로 session에 user가 존재하는지 아닌지에 따라 화면에 출력해주는 내용을 다르게 해준다   
onclick="location.href='/<url>/<url>/'" 을 통해 해당 버튼을 클릭하면 작성한 url로 이동할 수 있게 해준다

##### fcuser/home.html
```html
<div class="row mt-5">
    <div class="col-12 text-center">
        <h1>홈페이지</h1>
    </div>
</div>
<div class="row mt-5">
    {% if request.session.user %} # views.py에서 session유무 확인하는 코드를 생략하고 여기에 작성하였다
    <div class="col-12">
        <button class="btn btn-primary btn-block" onclick="location.href='/fcuser/logout/'">로그아웃</button>
    </div>
    {% else %}
    <div class="col-6">
        <button class="btn btn-primary btn-block" onclick="location.href='/fcuser/login/'">로그인</button>
    </div>
    <div class="col-6">
        <button class="btn btn-primary btn-block" onclick="location.href='/fcuser/register/'">회원가입</button>
    </div>
    {% endif %}
</div>
<div class="row mt-1">
    <div class="col-12">
        <button class="btn btn-primary btn-block" onclick="location.href='/board/list'">게시물 보기</button>
    </div>
</div>
```
<br>

📌views.py 작성하기 (bootstrap이용)    

user id를 session을 통해서 받은뒤 해당 user id가 존재하면 fcuser에 저장한 후 home 화면으로 랜더링 된다

##### fcuser/views.py
```python
def home(request):
    #user_id = request.session.get('user')
    #if user_id:
    #    fcuser = Fcuser.objects.get(pk=user_id)  #--> 해당 코드는 세션의 유무 확인 코드이다 home 템플릿에 작성할 수 있으므로 템플릿에                                                   # 작성해주자
        
    return render(request, 'home.html')

```
위에까지 작성한다면 버튼을 눌렀을때 해당 url로 이동하는 것을 볼 수 있다   
이렇게 게시판 글쓰기 버튼 , 돌아가기 버튼에도 onclick를 주면 된다  

<br>

📌게시글을 클릭했을때 상세보기가 가능할 수 있게 board_detail.html도 작성해준다    

tr 을 click 했을때 url의 끝부분에 id가 들어갈 수 있게 설정해준다. 이미 board/urls.py에 path('detail/<int:pk>/', views.board_detail)가 들어가있기 때문에 이동이 가능하다    

##### board/board_detail.html

```html
<tbody>
   {% for board in boards %}
   <tr onclick="location.href='/board/detail/{{board.id}}/'">
       <th>{{ board.id }}</th>
       <td>{{ board.title }}</td>
       <td>{{ board.writer }}</td>
       <td>{{ board.registered_dttm }}</td>
   </tr>
   {% endfor %}

</tbody>
```
<br>
