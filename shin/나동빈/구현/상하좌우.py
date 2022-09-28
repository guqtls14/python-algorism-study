n=int(input())
plans = input().split()
x,y=1,1

# L,R,U,D 이동
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

# 이동 계획 확인
for plan in plans:
    # 이동후 좌표확인
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    # 공간무시
    if nx < 1 or ny > 1 or nx>n or ny>n:
        continue
    # 이동 수행
    x,y=nx,ny
print(x,y)