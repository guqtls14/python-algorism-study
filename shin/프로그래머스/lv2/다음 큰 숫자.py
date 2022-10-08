

# bin은 10진수 -> 2진수로 바꾸는 함수, type은 str

def solution(s):
    a=bin(s).count('1')
    for i in range(s+1,999999):
        if bin(i).count('1') == a:
            return i

# def nextBigNumber(n):
#     num1 = bin(n).count('1')
#     while True:
#         n = n + 1
#         if num1 == bin(n).count('1'):
#             break
#     return n

    
s=78
print(solution(s))