n=int(input())

li=[list(map(int, input().split())) for _ in range(n)]

m=len(li)//2
n=len(li)//2

tmp=0

for i in range(len(li)):
    if i < len(li) // 2:
        tmp += sum(li[i][m:n+1])
        m-=1
        n+=1
    else:
        tmp += sum(li[i][m:n+1])
        m+=1
        n-=1
print(tmp)

# 강사님풀이
# res=0
# s=e=n//2

# for i in range(n):
#     for j in range(s,e+1):
#         res+=li[i][j]
#     if i<n//2:
#         s-=1
#         e+=1
#     else:
#         s+=1
#         e-=1
# print(res)