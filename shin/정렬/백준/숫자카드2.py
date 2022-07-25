import sys
n=int(sys.stdin.readline())
li1=list(map(int, sys.stdin.readline().split()))
m=int(sys.stdin.readline())
li2=list(map(int, sys.stdin.readline().split()))

di={}

for i in li2:
    if i not in li1:
        di[i] = 0
    else:
        cnt=li1.count(i)
        di[i] = cnt
for i in di.keys():
    print(di[i],end=' ')