# # 피보나치수

def solution(n):
    if n<3:
        return n
    d=[0]*(n+1)
    d[1]=1
    d[2]=2
    for i in range(3,n+1):
        d[i]=d[i-1]+d[i-2]
    return d[n]%1234567

# def jumpCase(num):
#     a, b = 1, 2
#     for i in range(2,num):
#         a, b = b, a+b
#     return b

print(solution(4))


# 피보나치
# def solution(num):
#     li=[0,1]
#     for i in range(2,num+1):
#         li.append(li[i-1]+li[i-2])
#     return li
# print(solution(9))