li = [list(map(int,input().split) for _ in range(7))]
cnt=0

# 가로
for i in range(3):
    for j in range(7):
        tmp=li[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt+=1
        # for else구문: for와 들여쓰기 위치 같아야함
        for k in range(2): # 5//2
            if li[i+k][j] != li[i+5-k-1]:
                break
        else:
            cnt+=1
print(cnt)