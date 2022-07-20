n=int(input())
li=[]
for _ in range(n):
    li.append(input())
li=list(set(li))
li=sorted(li,key=lambda x:(len(x),x))

for i in li:
    print(i)