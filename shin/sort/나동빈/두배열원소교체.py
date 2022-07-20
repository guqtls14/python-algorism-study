a,b=map(int, input().split())

ar1=list(map(int, input().split()))
ar2=list(map(int, input().split()))
ar1.sort()
ar2.sort(reverse=True)
print(ar2)
for i in range(b):
    if ar1[i] < ar2[i]:
        ar1[i],ar2[i] = ar2[i],ar1[i]
    else:
        break
print(sum(ar1))