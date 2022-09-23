"""
 *packageName    : 
 * fileName       : 2667.단지번호붙이기
 * author         : ipeac
 * date           : 2022-09-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-16        ipeac       최초 생성
 """
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 상 우 하 좌

n = int(input())
grid = [list(map(int, input())) for _ in range(n)]
# grid = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]

visited = [[0] * n for _ in range(n)]
answer = []

def bfs(row, col):
    q = deque()
    q.append([row, col])
    visited[row][col] = 1
    home_cnt = 1  # 집수 체크
    
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and grid[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = 1
                home_cnt += 1
    return home_cnt

cnt = 0  # 총 단지수
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and grid[i][j] == 1:
            cnt += 1  # 총 단지수
            mind = bfs(i, j)
            answer.append(mind)
answer.sort()
print(cnt)
for i in answer:
    print(i)
