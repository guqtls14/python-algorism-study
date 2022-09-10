"""
 *packageName    : 
 * fileName       : 2178.미로 탐색
 * author         : ipeac
 * date           : 2022-09-09
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-09        ipeac       최초 생성
 """

# n ; 세로 m ; 가로

from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(start):
    visited = [[0] * m for _ in range(n)]
    
    q = deque()
    q.append([start, start])
    visited[start][start] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or n <= nx or ny < 0 or m <= ny:
                # print("패스")
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])
    return graph[n - 1][m - 1]

n, m = map(int, input().split())
graph = []
for i in range(n):
    k = input()
    graph.append(list(map(int, k)))
# n, m = 4, 6
# graph = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]

print(bfs(0))
