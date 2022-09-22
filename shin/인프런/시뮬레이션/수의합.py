a,b=map(int, input().split())

li=list(map(int, input().split()))

cnt=0

lt=0
rt=1
tot=li[0]

while True:
    if tot<b:
        if rt<a:
            tot+=li[rt]
            rt+=1
        else:
            break
    elif tot == b:
        cnt+=1
        tot-=li[lt]
        lt+=1
    else:
        tot-=li[lt]
        lt+=1
print(cnt)