'''
#1. 다음 조건을 만족하는 함수 만들기
문자들 요소로 구성된 리스트를 인자로 받아, 문자열 길이가 2 이상이고 문자열의 첫번째와 마지막 문자가 같은 문자열의 수를 세는 start_end 함수를 작성해주세요! 
예시 input: start_end(['level', 'asdwe', 's', 'abceda', 'gsdwrtfg'])
output: 3
'''


# def start_end(my_list):
#     count_list=0
#     for i in range(len(my_list)):
#         len_word=len(my_list[i])
#         if len_word>=2 and my_list[i][0]==my_list[i][len_word-1]:
#             count_list=count_list+1
#     return count_list
# #input 함수는 string으로 받아드리므로 다시 list 화 시켜야한다
# str_input= input("start_end함수를 사용하려면 문자열을 space로 나누어 주세요(ex)adc mm asd adsa)    :")
# list_input=str_input.split()
# print(start_end(list_input))

'''
2. 솔로 천국 만들기 
리스트가 주어집니다. 리스트의 각 요소는 숫자 0부터 9까지로 이루어져 있습니다.

이때, 리스트에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다.

리스트에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 반환하는 lonely 함수를 작성해 주세요.

단, 제거된 후 남은 수들을 반환할 때는 리스트의 요소들의 순서를 유지해야 합니다.

lonely([1, 1, 3, 3, 0, 1, 1]) #=> [1, 3, 0, 1]
lonely([4,4,4,3,3]) #=> [4,3]
'''
def lonely(lone_list):
    new_lone_list=[]
    mediate=None
    for i in range(len(lone_list)):
        if lone_list[i]!=mediate:
            new_lone_list.append(lone_list[i])
            mediate=lone_list[i]
    return new_lone_list
print(lonely([0,4,4,4,3,3]))
            
        