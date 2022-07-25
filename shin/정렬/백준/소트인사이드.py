n=input()

li=[]

for i in n:
    li.append(i)
li=sorted(li,reverse=True)
print(''.join(li))