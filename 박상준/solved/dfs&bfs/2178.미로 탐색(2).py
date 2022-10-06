"""
 *packageName    : 
 * fileName       : 2178.미로 탐색(2)
 * author         : ipeac
 * date           : 2022-10-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-06        ipeac       최초 생성
 """
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# n, m = 4, 6
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
# graph = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]
visited = [[0] * m for _ in range(n)]
min_value = 1e9

def dfs(i, j, visited):
    global min_value
    x, y = i, j
    if x == n - 1 and y == m - 1:
        min_value = min(min_value, visited[x][y] + 1)
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 > nx or nx >= n or 0 > ny or ny >= m:
            continue
        else:
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                dfs(nx, ny, visited)
                visited[nx][ny] -= visited[x][y] + 1

# dfs(0, 0, visited) # dfs는 시간 초과난다... 재귀를 통해서 최대 깊이를 탐색하기에...
# print(min_value)
def bfs(i, j, visited):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    
    while q:
        x, y = q.popleft()
        for xx, yy in zip(dx, dy):
            nx, ny = x + xx, y + yy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
    print(visited[n - 1][m - 1])

bfs(0, 0, visited)
# bfs(0, 0)
