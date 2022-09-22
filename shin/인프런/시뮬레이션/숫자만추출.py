s=input()
answer=''
res=0
for x in s:
    if x.isdecimal():
        answer+=x
answer=int(answer)
print(answer)
cnt=0
for i in range(1,answer+1):
    if answer%i ==0:
        cnt+=1
print(cnt)