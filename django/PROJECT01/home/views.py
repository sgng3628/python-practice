from django.shortcuts import render, HttpResponse
from datetime import datetime
import random
import requests
import os

# Create your views here.
def index(request):
    return render(request, 'home/index.html')
    
def index2(request):
    return render(request, 'home/index2.html')
    
#자기소개 hola
def hola(request):
    return HttpResponse('My name is TaeWan')
    
#야식메뉴
def midnight(request):
    menus=['라면','떡볶이', '치킨', '피자']
    t_menu=random.choice(menus)
    return HttpResponse(f'오늘의 야식메뉴는 {t_menu}입니다')
    
#야식메뉴
def midnight2(request):
    menus=['라면','떡볶이', '치킨', '피자']
    t_menu=random.choice(menus)
    context={'menus':menus,'t_menu':t_menu}
    return render(request, 'home/midnight2.html', context)
    
#로또--6개--< range(1,46)
def lotto(request):
    numbers=range(1,46)
    my_lotto=random.sample(numbers, 6)
    real_lottos = [6,10,16,28,34,38]
    return render(request, 'home/lotto.html',{'my_lotto':my_lotto, 'real_lottos':real_lottos})
    
def dinner(request):
    menus=['chicken','bob', 'pizza']
    picked = random.choice(menus)
    return render(request, 'home/dinner.html', {'menus': menus, 'picked':picked})
    
def hello(request,name):
    return render(request, 'home/hello.html', {'name':name,})
    
def cube(request, num):
    nums=num**3
    return render(request, 'home/cube.html', {'num':num, 'nums':nums})
    
#이름 나이를 받아 tmeplate에서 (name)dml 나이는 age입니다.\

def introduce(request, name, age):
    return render(request, 'home/introduce.html', {'name':name, 'age':age})
    
def multiply(request, a, b):
    c=a*b
    return render(request, 'home/multiply.html', {'a':a,'b':b,'c':c})

def area(request, r):
    S=3.14*r*r
    return render(request, 'home/area.html', {'r': r, 'S':S})

def isbirth(request):
    today=datetime.now() 
    if today.month==9 and today.day==5:
        result=True
    else: result=False
    
    return render(request, 'home/isbirth.html', {'result':result})

def template_example(request):
    my_list=['짜장면','짬뽕', '탕수육','양장피']
    messages=['apple','hi', 'banana', 'mango']
    empty_list=[]
    return render(request, 'home/template_example.html',{'my_list':my_list, 'messages':messages, 'empty_list': empty_list})
    
    
def ping(request):
    return render(request, 'home/ping.html')

def pong(request):
    data = request.GET.get('data')
    return render(request,'home/pong.html',{'data':data})
    
def catch(request):
    return render(request, 'home/catch.html')
# artii API  를 통해 ascii 아트로 변환하여 보여주는 페이지
def result(request):
    #1. form 태그로 날린 데이터를 받는다.(GET방식)
    word=request.GET.get('word')
    #2. ARTII api 로 보낸 응답 결과를 text로 fonts라는 변수에 저장한다.
    fonts=requests.get('https://artii.herokuapp.com/fonts_list').text
    #3.fonts(str)를 fonts(list)로 바꿔준다.
    fonts=fonts.split('\n')
    #4.fonts(list)안에 들어있는 요소중 하나를 선택해서 font라는 변수에 저장한다.(랜덤)
    font=random.choice(fonts)
    #5.위에서 우리가 만든 word 와 font를 가지고 다시 arttii 로 요청을 보낸 후에 답을 응답결과를 result라는 변수에 저장한다
    result=requests.get(f'https://artii.herokuapp.com/make?text={word}&font={font}').text
    return render(request, 'home/result.html',{'result':result})
    
def throw(request):
    return render(request, 'home/throw.html')
    
def get(request):
    name=request.GET.get('name')
    numbers=range(1,46)
    my_lotto=random.sample(numbers, 6)
    return render(request, 'home/get.html',{'my_lotto':my_lotto,'name':name})
    
  
#POST 요청
def user_new(request):
    return render(request, 'home/user_new.html')

def user_create(requests):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    return render(request, 'home/user_create.html', {'name':name, 'pwd':pwd})

def static_example(request):
    return render(request, 'home/static_example.html')
    
def home(request):
    numbers=range(10)
    a=os.listdir("/home/ubuntu/workspace/django/PROJECT01/home/templates/home")
    return render(request, 'home/home.html', {'numbers':numbers, 'a':a})