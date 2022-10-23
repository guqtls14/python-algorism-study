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


price=[5,2,8,10,3]
print(solution(price))

# https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%8B%9D%EA%B0%80%EA%B2%A9-Python