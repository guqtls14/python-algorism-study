"""
"""
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# n ;x 축 m ; y축
# n, m = 8, 9
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
print(f"grid : {grid}")
# grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 1, 1, 0], [0, 0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# 격자 치즈 1 없는 0 ;;
# 2면이 없는 부분이라면 녹아서 없어진다. 모두 녹아 없어지는 걸리는 정확한 시간 출력

answer = 0

def out_minus_maker():
    dp = deque()
    dp.append([0, 0])
    out_visited = [[0] * m for _ in range(n)]
    out_visited[0][0] = 1
    grid[0][0] = -1
    while dp:
        x, y = dp.popleft()
        for xx, yy in zip(dx, dy):
            nx, ny = xx + x, yy + y
            if 0 > nx or 0 > ny or n <= nx or m <= ny:
                continue
            if grid[nx][ny] == 1 or out_visited[nx][ny] == 1:
                continue
            dp.append([nx, ny])
            grid[nx][ny] = -1
            out_visited[nx][ny] = 1
    return

# 치즈가 다 녹았는지 확인
def is_melt():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                return False
    return True

while not is_melt():
    out_minus_maker()  # 외부를 -1 로 초기화
    check = []  # 삭제될 친구
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:  # bfs수행 조건
                cnt = 0
                for x, y in zip(dx, dy):
                    nx, ny = i + x, j + y
                    if 0 > nx or 0 > ny or n <= nx or m <= ny:
                        continue
                    if grid[nx][ny] == -1:  # 외부와 접촉하는 면
                        cnt += 1
                if cnt >= 2:  # 4방향으로 돌면서 체크된 외부의 면과의 접촉 횟수
                    check.append([i, j])  # 없어질 친구
    for x, y in check:
        grid[x][y] = 0
    answer += 1

print(answer)
