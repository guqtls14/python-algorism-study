# word={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,"J":10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
# li=list(map(str, input()))

# for i in li:
#     print(word[i],end=' ')

# container = input()
# for i in container:
#     ans=ord(i)-64
#     print(ans,end=' ')

a=int(input())
li=[]
for i in range(1,a+1):
    if i in [3,6,9]:
        li.append('-'*[3,6,9].count(i))
    else:
        li.append(i)
for i in li:
    print(i,end=' ')