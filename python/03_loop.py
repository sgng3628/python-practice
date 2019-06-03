# numbers=[1,2,3,4,5,6]
# new_numbers=[]
# for num in numbers:
#     new_numbers.append(2*num)
# print(new_numbers)


nums=[1,2,3,4,5,6,7,8,9]
gugu=[]
a=[]

for i in nums:
    for j in nums:
        a.append(i*j)
    gugu.append(a)
    a=[]
print(gugu)
        
    