n=int(input())

numbers = list(map(int, input().split()))

numset = set(numbers)
list = list(numset)
list.sort()
# print(list)
numdict = {}
for i in range(len(list)):
    numdict[list[i]] = i

for i in numbers:
    print(numdict[i],end=' ')