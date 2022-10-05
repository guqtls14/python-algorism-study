from math import gcd

def solution(n):
    li=[]
    for _ in range(n):
        a,b=map(int,input().split())
        def answer(a,b):
            li.append(a*b//gcd(a,b))
        answer(a,b)
    return li

# print(solution(int(input())))
li1=solution(int(input()))
for i in li1:
    print(i)