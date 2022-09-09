"""
 *packageName    : 
 * fileName       : 1260_DFS와 BFS
 * author         : qkrtkdwns3410
 * date           : 2022-09-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-06        qkrtkdwns3410       최초 생성
 """
import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split(" "))

graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split(" "))
    graph[a][b] = graph[b][a] = 1

def bfs(v, visited):
    q = deque([v])
    
    # dfs 를 완료한 visitied 배열(0으로 되어 있음)
    visited[v] = 1
    
    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in range(1, n + 1):
            if visited[i] == 0 and graph[V][i] == 1:
                q.append(i)
                visited[i] = 1

def dfs(v, visited):
    visited[v] = 1
    print(v, end=" ")
    
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i, visited)

# n 정점의 개수 m 간선의 개수 탐색을 시작할 정점의 번호 v node : 간선이 연결하는 두 정점의 번호
def solution(n, v):
    visited_list1 = [0] * (n + 1)
    visitied_list2 = [0] * (n + 1)
    
    dfs(v, visitied_list2)
    print()
    bfs(v, visited_list1)

solution(n, v)
