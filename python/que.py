'''
# 1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?
# 8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
# (※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함)count_8=0
for i in range(1,10001):
    for j in str(i):
        if j=='8':
            count_8+=1

print(count_8)


# 숫자 형태의 문자열을 콤마가 포함된 금액 표기식 문자열로 바꾸어주는 프로그램을 작성하시오.
x='10000237753'
left=len(x)%3
if left==0:
    new=[]
    for i in range(0,int(len(x)/3)):
        new.append(x[3*i:3*(i+1)])
    print(",".join(new))
    
else:
    print(x[0:left], end=',')
    re_x=x[left:]
    new=[]
    for i in range(0,int(len(re_x)/3)):
        new.append(re_x[3*i:3*(i+1)])
    print(",".join(new))
'''

#숫자를 입력받고 --억 --만 --- 이런식으로 문자열로 바꿔어 주기
    
a=[1,2,3,4,5,6,7,8,9,4,5,4,1,1,1,1,1,2]
numbering=['만','억','조','경']
for i in range(0, int(len(a)/4)):
    a.insert(len(a)-4*(i+1)-i, numbering[i])
for j in a:
    print(j, end='')
print('')

