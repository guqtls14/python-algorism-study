n=int(input())

for k in range(n):
    li=[list(map(int,input().split())) for _ in range(5)]


    largest=-9999999
    # 가로,세로
    for i in range(5):
        sum1=sum2=0
        sum1=sum(li[i])
    
        for j in range(5):
            sum2 += li[j][i]
        if sum1 > largest:
            largest = sum1
        if sum2 > largest:
            largest = sum2
    # 대각선
    sum1=sum2=0
    for i in range(5):
        sum3=li[i][i]
        sum4=li[i][5-i-1]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum1
    print('#{} {}'.format(k,largest)) 