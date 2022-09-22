li=list(range(21))

for _ in range(10):
    s,e=map(int, input().split())
    for i in range((e-s+1)//2):
        li[s+i],li[e-i]=li[e-i],li[s+i]
li.pop(0)
print(*li)