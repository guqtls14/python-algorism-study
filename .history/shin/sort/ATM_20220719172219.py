n=int(input())

a=list(map(int, input().split()))
a.sort()
s=0
for i in range(len(a)-1,0,-1):
    s+=a[i]
    for j in range(i-1,0,-1):
        s+=a[j]
print(s)