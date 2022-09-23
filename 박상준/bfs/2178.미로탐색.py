"""
 *packageName    : 
 * fileName       : 2178.미로탐색
 * author         : ipeac
 * date           : 2022-09-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-19        ipeac       최초 생성
 """
from collections import deque

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
n, m = map(int, input().split())
# grid = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]
grid = []

for i in range(n):
    grid.append(list(map(int, input())))


def bfs(i):
    visited = [[0] * m for _ in range(n)]
    visited[i][i] = 1

    q = deque()
    q.append([i, i])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and grid[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
    return visited[n - 1][m - 1]


print(bfs(0))
