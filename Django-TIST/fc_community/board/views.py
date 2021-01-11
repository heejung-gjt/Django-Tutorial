from fcuser.models import Fcuser
from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm
from django.http import Http404
from django.core.paginator import Paginator

def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')
    
    return render(request, 'board_detail.html',{'board':board})

def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login/')
    if request.method == 'POST':  # 제목과 내용이 요청되었을때
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user') 
            fcuser = Fcuser.objects.get(pk=user_id) 

            board = Board()
            board.title = form.cleaned_data['title']    
            board.contents = form.cleaned_data['contents']  
            board.writer = fcuser 
            board.save()  # DB에 저장

            return redirect('/board/list')
    else:
        form = BoardForm()
    
    return render(request, 'board_write.html', {'form':form })

def board_list(request):
    board_all = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p',1))
    paginator = Paginator(board_all, 2)
    boards = paginator.get_page(page)
    return render(request, 'board_list.html',{'boards': boards}) #boards안에 이미 page에 대한 정보 들어가 있음