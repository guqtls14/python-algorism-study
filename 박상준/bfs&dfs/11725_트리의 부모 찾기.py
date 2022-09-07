"""
 *packageName    : 
 * fileName       : 11725_트리의 부모 찾기
 * author         : qkrtkdwns3410
 * date           : 2022-09-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-07        qkrtkdwns3410       최초 생성
 """
from collections import deque

def bfs(graph, start):
    q = deque([start])
    visited[start] = 1
    
    while q:
        start = q.popleft()
        for i in graph[start]:
            if visited[i] == 0:
                visited[i] = start
                q.append(i)
    return visited

n = int(input())
node = []

for i in range(n - 1):
    a, b = map(int, input().split(' '))
    node.append([a, b])

visited = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]
for i in node:
    a, b = i[0], i[1]
    graph[a].append(b)
    graph[b].append(a)
bfs(graph, 1)

for i in visited[2:]:
    print(i)
