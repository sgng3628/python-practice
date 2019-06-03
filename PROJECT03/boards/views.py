from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Board
from .forms import BoardForm

def index(request):
    boards=Board.objects.all()[::-1]
    return render(request, 'boards/index.html', {'boards':boards})

@login_required
def create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            # #cleanded_data-> dictionary 자료형으로 만들어줌(get을 사용할수 ㅇㅆ음)
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # board = Board.objects.create(title=title, content=content)
            board = form.save(commit=False)
            board.user = request.user
            board.save()
            return redirect('boards:detail', board.pk)
        
    else:
        form = BoardForm()
    return render(request, 'boards/form.html', {'form':form})
    # valid한 요청이 아닌 경우와 POST요청이 아닌 모든 경우를 return 하기 위해서 이렇게 작성
        
def detail(request, board_pk):
    board=get_object_or_404(Board, pk=board_pk)
    
    return render(request, 'boards/detail.html',{'board':board})

def delete(request, board_pk):
    board=get_object_or_404(Board, pk=board_pk)
    if board.user == request.user:
        
        if request.method == 'POST':
            board.delete()
            return redirect('boards:index')
        else:
            return redirect('boards:detail', board.pk)
    else: 
        return redirect('boards:index')
@login_required
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if board.user == request.user:
        
        if request.method == 'POST':
            # form = BoardForm(request.POST)
            form = BoardForm(request.POST, instance=board)
            if form.is_valid():
                # board.title = form.cleaned_data.get('title')
                # board.content = form.cleaned_data.get('content')
                # board.save()
                board=form.save()
                return redirect('boards:detail', board.pk)
    
        else: 
            # form = BoardForm(initial=board.__dict__)
            #create 와 다른점. 기존의 글들이 있음
            form = BoardForm(instance=board)
        return render(request, 'boards/form.html', {'form':form, 'board':board})
    else:
        return redirect('boards:index')

@login_required        
def like(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    user = request.user
    
    if board.like_users.filter(pk=user.pk).exists():
        board.like_users.remove(user)
    else:
        board.like_users.add(user)
    return redirect('boards:index')
    