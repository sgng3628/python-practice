'''
# 달력 만들기-1
days=[31,28,31,30,31,30,31,31,30,31,30,31]
all_day=[' ',' ']
for i in range(1,13):
    last_day=days[i-1]+1
    for day in range(1, last_day):
        all_day.append(day)
for i in range(1,13):
    print (f'{i}월')
    print('일  월  화  수  목  금  토')
    for week in range(4):
        for k in range(7): 
            print(all_day.pop(0), end=" ")
        print()


# 달력 만들기-2
days=[31,28,31,30,31,30,31,31,30,31,30,31]
all_day=[' ',' ']
for i in range(1,13):
    last_day=days[i-1]+1
    for day in range(1, last_day):
        all_day.append(day)
for i in range(1,10):
    print (f'{i}월')
    print('일  월  화  수  목  금  토')
    for week in range(5):
        for k in range(7): 
            c=all_day.pop(0)
            print(c, end=" ")
            if c==31: break
        print()

        

# 달력 만들기-3 성공
dict_cal={1:31, 2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
dict_space={1:2, 2:5, 3:5, 4:1, 5:3, 6:6, 7:1, 8:4, 9:0, 10:2, 11:5, 12:0}
for month in dict_cal.keys():
    print(f'{month}월')
    date=[]
    for i in range(dict_space[month]):
        date.append('  ')
    for j in range(1,dict_cal[month]+1):
        if j in range(10):
            digit=' '+str(j)
        else: digit=str(j)
        date.append(digit)
    print(' 일  월  화  수  목  금  토')
    for k in range(1, len(date)+1):
        if k%7==0:
            print(date[k-1])
            print()
        else: print(date[k-1], end="  ")
        
    print()
    print()
            


# 달력 만들기-4 성공(dict_space-> space)
dict_cal={1:31, 2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
space=2
for month in dict_cal.keys():
    print(f'{month}월')
    date=[]
    for i in range(space):
        date.append('  ')
    space=(space+dict_cal[month])%7
    for j in range(1,dict_cal[month]+1):
        if j in range(10):
            digit=' '+str(j)
        else: digit=str(j)
        date.append(digit)
    print(' 일  월  화  수  목  금  토')
    for k in range(1, len(date)+1):
        if k%7==0:
            print(date[k-1])
            print()
        else: print(date[k-1], end="  ")
        
    print()
    print()


# 달력 만들기-5 성공 앞으로 3년(윤년 계산 없이)
dict_cal={1:31, 2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
space=2
for year in range(2019,2022):
    print(f'{year}년')
    for month in dict_cal.keys():
        print(f'{month}월')
        date=[]
        for i in range(space):
            date.append('  ')
        space=(space+dict_cal[month])%7
        for j in range(1,dict_cal[month]+1):
            if j in range(10):
                digit=' '+str(j)
            else: digit=str(j)
            date.append(digit)
        print(' 일  월  화  수  목  금  토')
        for k in range(1, len(date)+1):
            if k%7==0:
                print(date[k-1])
                print()
            else: print(date[k-1], end="  ")
            
        print()
        print()


# 달력 만들기-6 성공 2019년 이후 달력(윤년 계산)
dict_cal={1:31, 2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
dict_cal2={1:31, 2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
space=2
#이 달력은 2019년을 기준으로 하여 그 이후의 일자를 계산할 수 있다. 만약 시작 년도를 바꾸려면 space를 그 시작년도 의 빈 공간으로 새로 설정해주어야한다.

for year in range(2019,2119):
    print(f'{year}년')
    #400으로 나누어 떨어지면 윤년
    if year%400==0:
        for month in dict_cal2.keys():
            print(f'{month}월')
            date=[]
            for i in range(space):
                date.append('  ')
            space=(space+dict_cal2[month])%7
            for j in range(1,dict_cal2[month]+1):
                if j in range(10):
                    digit=' '+str(j)
                else: digit=str(j)
                date.append(digit)
            print(' 일  월  화  수  목  금  토')
            for k in range(1, len(date)+1):
                if k%7==0:
                    print(date[k-1])
                    print()
                else: print(date[k-1], end="  ")
                
            print()
            print()
    
    #100으로 나누어 떨어지면 평년(400으로 나누어 떨어지지 않으며)
    elif year%100==0:
        for month in dict_cal.keys():
            print(f'{month}월')
            date=[]
            for i in range(space):
                date.append('  ')
            space=(space+dict_cal[month])%7
            for j in range(1,dict_cal[month]+1):
                if j in range(10):
                    digit=' '+str(j)
                else: digit=str(j)
                date.append(digit)
            print(' 일  월  화  수  목  금  토')
            for k in range(1, len(date)+1):
                if k%7==0:
                    print(date[k-1])
                    print()
                else: print(date[k-1], end="  ")
                
            print()
            print()
    #4로 나누어 떨어지면 윤년       
    elif year%4==0:
        for month in dict_cal2.keys():
            print(f'{month}월')
            date=[]
            for i in range(space):
                date.append('  ')
            space=(space+dict_cal2[month])%7
            for j in range(1,dict_cal2[month]+1):
                if j in range(10):
                    digit=' '+str(j)
                else: digit=str(j)
                date.append(digit)
            print(' 일  월  화  수  목  금  토')
            for k in range(1, len(date)+1):
                if k%7==0:
                    print(date[k-1])
                    print()
                else: print(date[k-1], end="  ")
                
            print()
            print()
    #나머지
    else:
        for month in dict_cal.keys():
            print(f'{month}월')
            date=[]
            for i in range(space):
                date.append('  ')
            space=(space+dict_cal[month])%7
            for j in range(1,dict_cal[month]+1):
                if j in range(10):
                    digit=' '+str(j)
                else: digit=str(j)
                date.append(digit)
            print(' 일  월  화  수  목  금  토')
            for k in range(1, len(date)+1):
                if k%7==0:
                    print(date[k-1])
                    print()
                else: print(date[k-1], end="  ")
                
            print()
            print()
'''

#달력만들기 년도/월을 input 받고 그 달의 달력만 보여주기
dict_cal={1:31, 2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31,'delay':1}
dict_cal2={1:31, 2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31,'delay':2}

origin_dealy_2001=1
input_year=int(input('연도를 입력하세요.'))
input_month=int(input('월을 입력하세요.'))

space=origin_dealy_2001
#2001년을 이후 delay 1
for year in range(2001,input_year):
    if year%400==0:
        space+=dict_cal2['delay']
    elif year%100==0:
        space+=dict_cal['delay']
    elif year%4==0:
        space+=dict_cal2['delay']
    else:
        space+=dict_cal['delay']


if input_year%400==0:
    for month in range(1,input_month):
        space+=dict_cal2[month]
    
    print(f'{input_year}년 {input_month}월')
    date=[]
    for i in range(space%7):
        date.append('  ')
    for j in range(1,dict_cal2[input_month]+1):
        if j in range(10):
            digit=' '+str(j)
        else: digit=str(j)
        date.append(digit)
    print(' 일  월  화  수  목  금  토')
    for k in range(1, len(date)+1):
        if k%7==0:
            print(date[k-1])
            print()
        else: print(date[k-1], end="  ")
        
    print()
    print()

elif input_year%100==0:
    for month in range(1,input_month):
        space+=dict_cal[month]
    
    print(f'{input_year}년 {input_month}월')
    date=[]
    for i in range(space%7):
        date.append('  ')
    for j in range(1,dict_cal[input_month]+1):
        if j in range(10):
            digit=' '+str(j)
        else: digit=str(j)
        date.append(digit)
    print(' 일  월  화  수  목  금  토')
    for k in range(1, len(date)+1):
        if k%7==0:
            print(date[k-1])
            print()
        else: print(date[k-1], end="  ")
        
    print()
    print()

elif input_year%4==0:
    for month in range(1,input_month):
        space+=dict_cal2[month]
    
    print(f'{input_year}년 {input_month}월')
    date=[]
    for i in range(space%7):
        date.append('  ')
    for j in range(1,dict_cal2[input_month]+1):
        if j in range(10):
            digit=' '+str(j)
        else: digit=str(j)
        date.append(digit)
    print(' 일  월  화  수  목  금  토')
    for k in range(1, len(date)+1):
        if k%7==0:
            print(date[k-1])
            print()
        else: print(date[k-1], end="  ")    
        
else:
    for month in range(1,input_month):
        space+=dict_cal[month]
    
    print(f'{input_year}년 {input_month}월')
    date=[]
    for i in range(space%7):
        date.append('  ')
    for j in range(1,dict_cal[input_month]+1):
        if j in range(10):
            digit=' '+str(j)
        else: digit=str(j)
        date.append(digit)
    print(' 일  월  화  수  목  금  토')
    for k in range(1, len(date)+1):
        if k%7==0:
            print(date[k-1])
            print()
        else: print(date[k-1], end="  ")
        
    print()
    print()
        



        
    