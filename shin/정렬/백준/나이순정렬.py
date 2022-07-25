n=int(input())
li=[]
for _ in range(n):
    li.append(input().split())
li=sorted(li,key=lambda x:(int(x[0])))

for i in li:
    print(i[0],i[1])