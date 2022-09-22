a,k=map(int, input().split())

li = list(map(int, input().split()))


m=0
n=0
cnt=0
# n == a 일때 까지 반복
while n<=a:
    if sum(li[m:n+1]) == k:
        if li[m] == li[n]:
            cnt+=1
            n+=1
        else:
            cnt+=1
            m+=1
        if m > n:
            break
    elif sum(li[m:n+1]) < k:
        n+=1
    elif sum(li[m:n+1]) > k:
        m+=1
print(cnt)