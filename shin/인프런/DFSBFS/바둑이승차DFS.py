# 부분집합문제와 거의유사

# L은 인덱스번호,부분집합의합(부분집합의합 문제와유사)
def DFS(L,sum):
    global result
    if sum>c:
        return

    if L==n:
        if sum > result:
            # global안쓰면 result는 local변수이므로 에러가나기에 global선언해줘야함
            result=sum
    else:
        DFS(L+1,sum+a[L])
        DFS(L+1,sum)


c,n=map(int,input().split())
a=[0]*n
result=-11111111
for i in range(n):
    a[i]=int(input())
DFS(0,0)
print(result)