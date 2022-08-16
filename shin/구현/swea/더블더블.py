n=int(input())
tmp=1
for i in range(1,n+2):
    if i == 1:
        print(i,end=' ')
    else:
        tmp=tmp*2
        print(tmp,end=' ')