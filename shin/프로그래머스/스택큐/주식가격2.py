# 이렇게풀면 효율성에서 떨어짐

# def solution(prices):
#     answer = []

#     while prices:
#         tmp=0
#         tmpword= prices.pop(0)
#         for i in prices:
#             # 떨어지기까지 시간이 1초가걸리므로 무조건 1초는 + 해야함
#             tmp+=1
#             if tmpword > i:
#                 break
#         answer.append(tmp)
#         tmp=0

#     return answer

from collections import deque

def solution(price):
    price1=deque(price)
    answer=[]

    while price1:
        tmp=0
        tmpword= price1.popleft()
        for i in price1:
            # 떨어지기까지 시간이 1초가걸리므로 무조건 1초는 + 해야함
            tmp+=1
            if tmpword > i:
                break
        answer.append(tmp)
        tmp=0
    return answer

prices=[1,2,3,2,3]
print(solution(prices))