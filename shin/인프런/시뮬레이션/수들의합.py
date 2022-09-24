# a,k=map(int, input().split())

# li = list(map(int, input().split()))


# m=0
# n=0
# cnt=0
# # n == a 일때 까지 반복
# while n<=a:
#     if sum(li[m:n+1]) == k:
#         if li[m] == li[n]:
#             cnt+=1
#             n+=1
#         else:
#             cnt+=1
#             m+=1
#         if m > n:
#             break
#     elif sum(li[m:n+1]) < k:
#         n+=1
#     elif sum(li[m:n+1]) > k:
#         m+=1
# print(cnt)

# 위에껀 오답

a,k=map(int, input().split())

li = list(map(int, input().split()))


lt=0
rt=1
tmp=li[0]
cnt=0

while True:
    if tmp<k:
        if rt<a:
            tmp+=li[rt]
            rt+=1
        else:
            break
    elif tmp == k:
        cnt+=1
        tmp-=li[lt]
        lt+=1
    else:
        tmp-=li[lt]
        lt+=1
print(cnt)