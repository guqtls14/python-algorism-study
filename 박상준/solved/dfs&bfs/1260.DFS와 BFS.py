"""
 *packageName    : 
 * fileName       : 1260.DFS와 BFS
 * author         : ipeac
 * date           : 2022-10-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-05        ipeac       최초 생성
 """
from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# pprint.pprint(graph)
# graph = [[0, 0, 0, 0, 0],
#          [0, 0, 1, 1, 1],
#          [0, 1, 0, 0, 1],
#          [0, 1, 0, 0, 1],
#          [0, 1, 1, 1, 0]]

def dfs(v, visited):
    visited[v] = 1
    print(v, end=" ")
    for i in range(1, n + 1):
        
        if visited[i] == 0 and graph[v][i] == 1:
            visited[i] = 1
            dfs(i, visited)

def bfs(v, visited):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        c = q.popleft()
        print(c, end=" ")
        
        for i in range(1, n + 1):
            if visited[i] == 0 and graph[c][i] == 1:
                q.append(i)
                visited[i] = 1

visited1 = [0] * (n + 1)
visited2 = [0] * (n + 1)
dfs(v, visited2)
print()
bfs(v, visited1)
