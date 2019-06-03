'''
#list 중 가장 큰 값/가장 작은 값

def max_list(a_list):
    mediate=a_list[0]
    for elem in a_list:
        if elem>mediate:
            mediate= elem
    return mediate

print(max_list([-1,-3,-4,-2,-1]))

# --> WTF; sort 한 후에 마지막을 뽑으면됨;;
def max_list(a_list):
    a_list.sort()
    return a_list[-1]

print(max_list([+71,-3,-4,-2,-1]))

# --> WTF*3
print(max([+71,-3,-4,-2,-1]))


# 표준 입력으로 정수 두 개가 입력됩니다(첫 번째 입력 값의 범위는 1~20, 두 번째 입력 값의 범위는 10~30이며 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다).
# 첫 번째 정수부터 두 번째 정수까지를 지수로 하는 2의 거듭제곱 리스트를 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).
# 단, 리스트의 두 번째 요소와 뒤에서 두 번째 요소는 삭제한 뒤 출력하세요. 출력 결과는 리스트 형태라야 합니다.

# a,b= int(input().split()) <-  map을 사용해라


x= input().split()
m=map(int,x)
a,b=m

my_list=[2**(i+1) for i in range(a,b) if i!=b-2 or i!=a+1]
print(my_list)
'''



#3. 영어 이름은 가운데 이름을 가지고 있는 경우가 있습니다.
# 가운데 이름은 축약해서 나타내는 함수를 작성해보세요.

# 예시 입력)
# Alice Betty Catherine Davis

# 예시 출력)
# Alice B. C. Davis

# -1.
# name_list=input().split()
# mid_name=name_list[1:len(name_list)-1]
# short_mid_name=[]
# for i in mid_name:
#     short_mid_name.append(i[0])
# print(name_list[0], end=' ')
# for str in short_mid_name:
#     print(str, end=' ')
# print(name_list[-1])




# -2. if 구문을 통하여 처음과 끝을 다른 방식으로 프린팅(이 문제에서는 .을 포함시켜야 함으로 이 방법이 조금 짧게 가능함)
name_list=input().split()
for i in range(0,len(name_list)):
    if i==0 or i==len(name_list)-1:
        print(name_list[i], end=" ")
    else:
        print(name_list[i][0], end=". ")
'''       
#-3. for 구문을 사용하여 리스트 자체를 변화 시킴(.을 포함시키기 위해선 위에 처럼 조건문을 다시 활용해야함)
name_list=input().split()
for i in range(1,len(name_list)-1):
    name_list[i]=name_list[i][0]
for j in name_list:
    print(j, end=" ")
'''