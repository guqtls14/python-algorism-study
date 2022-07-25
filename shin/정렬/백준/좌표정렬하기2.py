n=int(input())
li=[]
for _ in range(n):
    n,m=input().split()
    li.append((int(n),int(m)))
li=sorted(li,key=lambda x:(x[1],x[0]))
for i in range(len(li)):
    print(li[i][0],li[i][1])