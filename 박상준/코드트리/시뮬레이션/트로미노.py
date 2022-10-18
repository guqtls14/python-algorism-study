"""
 *packageName    : 
 * fileName       : 트로미노
 * author         : ipeac
 * date           : 2022-10-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-18        ipeac       최초 생성
 """
# n* m 차원
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# print(f"n,m = {n, m}")
# print(f"graph = {graph}")
# n, m = (3, 3)
# graph = [[1, 2, 3], [3, 2, 1], [3, 1, 1]]
visited = [[0] * m for _ in range(n)]

sum_t = 0
max_value = 0

# dfs + 시뮬
def dfs(i, j, depth, d_sum):
    global max_value
    
    if depth == 3:
        max_value = max(max_value, d_sum)
        return
    visited[i][j] = 1
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        
        if 0 > nx or n <= nx or 0 > ny or m <= ny:
            continue
        if not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, depth + 1, d_sum + graph[nx][ny])
            visited[nx][ny] = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 0, 0)
        visited[i][j] = 0
print(max_value)
