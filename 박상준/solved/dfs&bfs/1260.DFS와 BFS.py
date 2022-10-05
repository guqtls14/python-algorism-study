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

n, m, v = 4, 5, 1
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(f"graph : {graph}")

def dfs(v):
    pass

def bfs(v):
    q = deque()
    q.append([v])
    visited = [0] * (n + 1)
    while q:
        c = q.popleft()
        q.append(graph[c])
        pass
