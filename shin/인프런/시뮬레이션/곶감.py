n=int(input())

li=[list(map(int, input().split())) for _ in range(n)]


m=int(input())

# 배열 append,insert,pop개념
for _ in range(m):
    a,b,c=map(int, input().split())
    if b == 0:
        for _ in range(c):
            li[a-1].append(li[a-1].pop(0))
    else:
        for _ in range(c):
            li[a-1].insert(0,li[a-1].pop())

# 덧셈
q=0
e=n

tmp=0

for i in range(len(li)):
    if i < len(li) // 2:
        tmp += sum(li[i][q:e])
        q+=1
        e-=1
    else:
        tmp += sum(li[i][q:e])
        q-=1
        e+=1
print(tmp)