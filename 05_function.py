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
'''
def id(num):
    new_num=num//1000000
    if new_num%2:
        print('man')
    else:
        print('woman')

id(9609052333333)