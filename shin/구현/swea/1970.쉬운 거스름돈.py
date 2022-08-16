# a=[50000,10000,5000,1000,500,100,50,10]

# n=int(input())
# li=[]
# for i in range(len(a)):
#     if n // a[i] != 0:
#         li.append(n//a[i])
#         n=n%a[i]
#     else:
#         li.append(0)
# print(*li)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a=[50000,10000,5000,1000,500,100,50,10]
    print('#{}'.format(test_case))
    n=int(input())
    li=[]
    for i in range(len(a)):
        if n // a[i] != 0:
            li.append(n//a[i])
            n=n%a[i]
        else:
            li.append(0)
    print(*li)