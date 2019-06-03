'''
#클래스 정의
class Person:
    name = '아이유'
    
    def say_hello(self):
        print(f'Hello!, {self.name}')
        
iu=Person()
iu.say_hello()
print(iu.name)

Person.say_hello(iu)

iu.name='홍길동'
print(iu.name)
print(Person.name)

iu.say_hello()
Person.say_hello(iu)

print(isinstance(iu, Person))
class Student:
    pass
    
print(isinstance(iu, Student))

#클래스 용어
class Person: #클래스 정의
    name = 'tim' #맴버 변수
    
    def greeting(self):#멤버 메서드
        print(f'Hello!, {self.name}')
        
Tim=Person()#TIm-> Person 클래스의 instanse
Tim.greeting()
Tim.name

#3. self?
class Person:
    name = '아이유'
    age = '19'
    
    def greeting(self):
        print(f"Hello!, my name is {self.name}. I'm {self.age} years old".)

iu = Person()
iu.greeting()
print(iu.name)
print(iu.age)

#4

word='Not Class Member'

class Something:
    word='Class Member'
    
    def Set(self,msg):
        self.word = msg
    
    def Print(self):
        print(self.word)

g=Something()
g.Set('First Member')
g.Print()


class Person:
    def __init__(self, **kwargs):    # 키워드 인수
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']
 
maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
maria2 = Person(**{'name': '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})
print(maria1)
print(maria2)

#__init__ __del__
class Person:
    def __init__(self):
        print('응애')
    def __del__(self):
        print('빠이')
p1=Person()

class Myclass:
    def __init__(self,value):
        self.value=value
        print(f'{self.value}가 생성되엇습니다')
    def __del__(self):
        print('소멸되었습니다.')

def foo():
    d=Myclass(10)
foo()

#고민되는 부분 왜?
class Person:
    bag = []
 
    def put_bag(self, stuff):
        self.bag.append(stuff)
 
james = Person()
james.put_bag('책')
 
maria = Person()
maria.put_bag('열쇠')
 
print(james.bag)
print(maria.bag)
print(Person.bag)

class Person:
    populatuon=0
    
    def asd(self, name):
        self.name=name
        self.populatuon +=1
me=Person()
me.asd('tw')
friend=Person()
friend.asd('asd')
print(Person.populatuon)

class Person:
    populatuon=0
    
    def __init__(self, name):
        self.name=name
        Person.populatuon +=1
me=Person('tw')
print(me.name)
friend=Person('asd')
print(friend.name)
print(Person.populatuon)


class MixedNames:
    
    data='spam'
    
    def __init__(self, value):
        self.data = value
    def display(self):
        print(self.data, MixedNames.data)
        
x=MixedNames(1)
y=MixedNames(2)
x.display()
y.display()

#상속
class Person:
    def __init__(self,name):
        self.name=name
    def greeting(self):
        print(f'안녕하세요.저는 {self.name}입니다.')
class Student(Person):
    def __init__(self, name , student_id):
        self.name= name
        self.student_id: student_id
    def greeting(self):
        print(f'안녕하세요. 저는 {self.name}입니다. 저의 학번은 {self.student_id}입니다.')
s1=Student('Tim','123456')
s1.greeting()


#실습1
class Person:
    name='김 태 완'
    age='19'
    major='physics'
    
    def greeting(self):
        print(f'{self.name}{self.age}{self.major}')
        
i=Person()
i.greeting()
'''

#실습2
class Teacher():
    def __init__(self, name, subject):
        self.name=name
        self.subject=subject
    def intro(self):
        print(f'{self.name}선생님은 {self.subject}를 가르치신다.')

class Student():
    def __init__(self, name, subject):
        self.name=name
        self.subject=subject
    def intro(self):
        print(f'{self.name}학생은 {self.subject}를 좋아한다.')

Tim=Teacher('TIm',"Science")
Tim.intro()
Eric=Student('Eric','Math')
Eric.intro()