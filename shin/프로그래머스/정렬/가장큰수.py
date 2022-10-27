# 시간초과
# from itertools import permutations

# def solution(num):
#     permute = list(permutations(num,len(num)))
#     print(permute)
#     list_permute = [''.join(map(str,i)) for i in permute]   
#     print(list_permute)
#     answer = max(list_permute)
    
#     return answer

def solution(num):
    
    num = list(map(str, num))
    num.sort(key = lambda x : x*3, reverse = True)
    print(num)
    return str(int(''.join(num)))
# ???


# numbers=[6, 10, 2]	
numbers=[3, 30, 34, 5, 9]	
print(solution(numbers))

# 리스트(원소는int)를 문자열로만들고싶을때:''.join(map(str,i))
# ''.join(map(str,iteral))이유:https://computer-science-student.tistory.com/361