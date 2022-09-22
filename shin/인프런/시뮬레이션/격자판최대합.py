n=int(input())

li=[list(map(int, input().split())) for _ in range(n)]

tmp1=0
tmp2=0
tmp=-21321321
for i in range(n):
    tmp1=tmp2=0
    for j in range(n):
        tmp1+=li[i][j]
        tmp2+=li[j][i]
    tmp=max(tmp1,tmp2,tmp)
tmp1=tmp2=0

for i in range(n):
    tmp1+=li[i][i]
    tmp2+=li[i][n-i-1]
tmp=max(tmp,tmp1,tmp2)
print(tmp)