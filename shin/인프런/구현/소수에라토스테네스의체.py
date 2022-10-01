n=int(input())
cnt=0

ch=[0]*(n+1)

for i in range(2,n+1):
    if ch[i]==0:
        cnt+=1
        # i의 배수에 해당하는 인덱스도표시(소수가아니므로)
        for j in range(i,n+1,i):
            ch[j]=1
print(cnt)