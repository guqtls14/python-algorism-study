"""
 *packageName    : 
 * fileName       : 2667.단지번호붙이기[bfs&dfs]
 * author         : qkrtkdwns3410
 * date           : 2022-09-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-12        qkrtkdwns3410       최초 생성
 """
from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

cnt = 0
answer = []

# 그래프가 1 이고 방문 x한 경우 bfs가 수행된다,.
def bfs(x, y):
    global cnt
    visited[x][y] = 1
    cnt += 1
    each_cnt = 1
    q = deque()
    q.append((x, y))
    
    while q:
        ax, ay = q.popleft()
        for i in range(4):
            nx, ny = ax + dx[i], ay + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    each_cnt += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return each_cnt

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
# graph = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            answer.append(bfs(i, j))
answer.sort()
print(cnt)
for v in answer:
    print(v)
