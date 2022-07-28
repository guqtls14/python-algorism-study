n=int(input())

for _ in range(n):
    a=int(input())
    li=list(map(int, input().split()))
    print(min(li),max(li))