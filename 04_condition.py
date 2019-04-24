'''
if False:
    print('false')
else:
    print('true')


num=int(input('숫자를 입력해주세요:'))

if num %2 ==1:
    print('홀수입니다.')
else:
    print('짝수입니다.')

    
#1
dirt=float(input('미세먼지 농도를 입력해주세요:'))

if dirt<30:
    print('미세먼지 농도가 "좋음"입니다')
elif dirt<80:
    print('미세먼지 농도가 "보통"입니다')
elif dirt<150:
    print('미세먼지 농도가 "나쁨"입니다')
else:
    print('미세먼지 농도가 "매우나쁨"입니다')
'''

#2
mission=list(range(1,11))
odd_mission=[]
even_mission=[]
for num in mission:
    if num%2==1:
        odd_mission.append(num)
    else:
        even_mission.append(num)
        
print (odd_mission,even_mission)