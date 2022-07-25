li=[]
for _ in range(9):
    li.append(int(input()))
ar=[]
for i in range(len(li)-1):
    for j in range(i+1,len(li)):
        if sum(li) - (li[i]+li[j]) == 100:
            num1,num2=li[i],li[j]
            break
li.remove(num1)
li.remove(num2)
li.sort()

for i in li:
    print(i) 