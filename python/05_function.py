'''
height=30
width=20
area= height*width
perimeter= 2*(height+width)
print(f'직사각형의 넓이는 {area}이고, 둘레는 {perimeter}입니다.')

def square(height, width):
    area= height*width
    perimeter= 2*(height+width)
    print(f'직사각형의 넓이는 {area}이고, 둘레는 {perimeter}입니다.')

square(30,20)

def sum(a,b):
	result=a+b
    return result
c=sum(2,4)
print(c)


def say():
    return 'hi'
print(say())

def say(name, age):
    print(f'제이름은 {name}이고, 나이는 {age}입니다')
a=say('Taewan', 13)
print(a)


def my_max(a,b):
    if a>=b:
        return a
    else: return b
    
def my_min(a,b):
    if a<=b:
        return a
    else: return b

print(my_max(3,7))
print(my_min(4,5))


#인자로 두수를 넘겨서 곱한 값을 return 하는 함수
def my_multi(a,b):
    multi=a*b
    return multi

print(my_multi(3,6))
 
#원의 면적을 구하는 함수 만들기
def my_circle(r):
    size=3.14*r*r
    return size
print(my_circle(3))
#주민번호를-> 남자/여자인지 판단하는 함수

def id(num):
    new_num=num//1000000
    if new_num%2:
        print('man')
    else:
        print('woman')

id(9609052333333)

def greeting(age, name='jeju'):
    print(f'{name}은 {age}살 입니다')

greeting(19)
greeting(19,'taewan')
greeting(age=19, name='taewan')
greeting(name='taewan', age=19)
greeting(name='taewan', 19)(<-오류)

print(sep='-','hi','hi',)


def my_func(*args):
    print(args)
    print(type(args))
    return args
my_func(1,2,3,[4,3],{1:2,2:'a'})


def my_dict(**kwargs):
    print(kwargs)
    print(type(kwargs))

my_dict(한국어='안녕하세요', 영어='hi',중국어='니하오')

def my_dict(**kwargs):
    print(kwargs)
    print(type(kwargs))

my_dict(한국어:'안녕하세요', 영어:'hi',중국어:'니하오')

def my_dict(**kwargs):
    print(kwargs)
    print(type(kwargs))

my_dict('한국어':'안녕하세요', '영어':'hi','중국어':'니하오')

#실습1. 사용자 입력값(정수)을 받아서 짝홀 구분
def distin(n):
    if n%2==1:
        print('홀수')
    else:
        print('짝수')
num= int(input())
distin(num)

#실습2 리스트 안 가장 작은요소
items=[1,2,-8,0]

def small(it):
    it.sort()
    print(it[0])
small(items)

#실습3 양수값만 합
def positive_sum(*args):
    sum=0
    for i in args:
        if i>0:
            sum+=i
    print(sum)
positive_sum(1,-4,7,12)
'''
def my_dict(**kwargs):
    print(kwargs)
    print(type(kwargs))

my_dict(2='안녕하세요', 3='hi', 1='니하오')