n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

result=0

for _ in range(n):
    result += min(a) * max(b)
    a.remove(min(a))
    b.remove(max(b))
print(result)

# https://alpyrithm.tistory.com/6
# https://velog.io/@zwooo96/%EB%B0%B1%EC%A4%80-1026%EB%B2%88-%EB%B3%B4%EB%AC%BC-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython