a=int(input())
li1=list(map(int, input().split()))
b=int(input())
li2=list(map(int, input().split()))
p1=p2=0

answer=[]
while  len(li1) != p1 and len(li2) != p2:
    if li1[p1] > li2[p2]:
        answer.append(li2[p2])
        p2+=1
    elif li1[p1] < li2[p2]:
        answer.append(li1[p1])
        p1+=1
    else:
        answer.append(li1[p1])
        answer.append(li2[p2])
        p1+=1
        p2+=1
if len(li1) == p1:
    answer.extend(li2[p2:])
else:
    answer.extend(li1[p1:])
print(*answer)