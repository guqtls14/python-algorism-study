"""
 *packageName    : 
 * fileName       : 10026.적록색약
 * author         : qkrtkdwns3410
 * date           : 2022-09-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-20        qkrtkdwns3410       최초 생성
 """
import sys

sys.setrecursionlimit(10 ** 6)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = 5

ret = 0
ret_di = 0
# grid = [list(map(str, input())) for _ in range(n)]
grid = [['R', 'R', 'R', 'B', 'B'], ['G', 'G', 'B', 'B', 'B'], ['B', 'B', 'B', 'R', 'R'], ['B', 'B', 'R', 'R', 'R'],
        ['R', 'R', 'R', 'R', 'R']]


def dfs(cx, cy, c):
    visited[cx][cy] = 1
    for x, y in zip(dx, dy):
        nx, ny = cx + x, cy + y
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and grid[nx][ny] == c:
                dfs(nx, ny, c)


visited = [[0] * n for _ in range(n)]

for i in range(n):  # 적녹색약이 아닌 경우
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j, grid[i][j])
            ret += 1

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'R':
            grid[i][j] = 'G'

visited = [[0] * n for _ in range(n)]

for i in range(n):  # 적녹색약인  경우
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j, grid[i][j])
            ret_di += 1
print(ret)
print(ret_di)
