num,m =map(int,input().split())
num=list(map(int,str(num)))
stack=[]

for x in num:
    # 새로 stack이라는 배열을 만들고 해당 배열의 마지막과 기존배열의 첫번쨰와 비교했을때 만일 stack부분이 더작으면 마지막 stack원소를 빼는식으로전개
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    #  파이썬 코드실행시 순차적으로 실행이되고 해당 풀이에서 반복문에서 나오면 무조건 마지막수를 stack에 더하는식으로 코드를 작성
    stack.append(x)
if m !=0:
    stack=stack[:-m]
for i in stack:
    print(i,end='')



    