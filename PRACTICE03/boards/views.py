from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Board
from .forms import BoardForm
from accounts.forms import RegistrationForm
from accounts.models import Profile
import openpyxl

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
            board=form.save()
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
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)

@login_required
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
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
    
    
def user_data(request):
    # board = get_object_or_404(Board, pk=board_pk)

    user = request.user
    profile = user.profile

    if profile.gender == 'M':
        calorie= int(662-9.53*profile.age+(15.91*profile.weight+5.396*profile.height)*(0.87+0.13*int(profile.activity)))
    else:
        calorie= int(354-6.91*profile.age+(9.36*profile.weight+7.26*profile.height)*(0.87+0.13*int(profile.activity)))
    
    carbohydrate_low= int(calorie*0.55/4)
    carbohydrate_high= int(calorie*0.65/4)
    protein_low= int(calorie*0.07/4)
    protein_high= int(calorie*0.2/4)
    fat_low= int(calorie*0.15/9)
    fat_high= int(calorie*0.3/9)
    profile.calorie=calorie
    profile.carbohydrate_low=carbohydrate_low
    profile.carbohydrate_high=carbohydrate_high
    profile.protein_low=protein_low
    profile.protein_high=protein_high
    profile.fat_low=fat_low
    profile.fat_high=fat_high
    
    profile.save()
    return render(request, 'boards/calculator.html',{'calorie':calorie,'carbohydrate_low':carbohydrate_low,'carbohydrate_high':carbohydrate_high,'protein_low':protein_low,'protein_high':protein_high,'fat_low':fat_low,'fat_high':fat_high})

def select_food(request):
    # board = get_object_or_404(Board, pk=board_pk)
    
    if request.method == 'POST':
        wb= openpyxl.load_workbook('food.xlsx')
        ws = wb.active
        food1 = request.POST.get('food1')
        food2 = request.POST.get('food2')
        food3 = request.POST.get('food3')
        quantity1 = float(request.POST.get('quantity1'))
        quantity2 = float(request.POST.get('quantity2'))
        quantity3 = float(request.POST.get('quantity3'))
        for r in ws.rows:
            if r[0].value == food1:
                calorie1 = int(r[1].value*quantity1)
                carbohydrate1 = int(r[2].value*quantity1)
                protein1 = int(r[3].value*quantity1)
                fat1 = int(r[4].value*quantity2)
            
            elif r[0].value == food2:
                calorie2 = int(r[1].value*quantity2)
                carbohydrate2 = int(r[2].value*quantity2)
                protein2 = int(r[3].value*quantity2)
                fat2 = int(r[4].value*quantity2)
            
            elif r[0].value == food3:
                calorie3 = int(r[1].value*quantity3)
                carbohydrate3 = int(r[2].value*quantity3)
                protein3 = int(r[3].value*quantity3)
                fat3 = int(r[4].value*quantity3)
        
        sum_calorie=calorie1+calorie2+calorie3  
        sum_carbohydrate=carbohydrate1+carbohydrate2+carbohydrate3
        sum_protein=protein1+protein2+protein3
        sum_fat=fat1+fat2+fat3
        
        return render(request,'boards/food.html',{'food1':food1, 'calorie1':calorie1,'carbohydrate1':carbohydrate1,'protein1':protein1, 'fat1':fat1,'food2':food2, 'calorie2':calorie2,'carbohydrate2':carbohydrate2,'protein2':protein2, 'fat2':fat2,'food3':food3, 'calorie3':calorie3,'carbohydrate3':carbohydrate3,'protein3':protein3, 'fat3':fat3,'sum_calorie':sum_calorie,'sum_carbohydrate':sum_carbohydrate,'sum_protein':sum_protein,'sum_fat':sum_fat,})
    else:
        return render(request,'boards/input.html')