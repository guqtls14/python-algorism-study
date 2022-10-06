"""
 *packageName    : 
 * fileName       : 11725.트리의 부모 찾기(2)
 * author         : ipeac
 * date           : 2022-10-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-06        ipeac       최초 생성
 """
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

# 노드의 개수 N
n = int(input())
# n=int(input())

# 2차 배열 -> 1차배열로 변경
graph = [[] for _ in range(n + 1)]
# n-1 개의 줄에 트리 상에서 연결된 두 정점.
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# graph = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0]]
# visited = [0] * (n + 1)
visited2 = [0] * (n + 1)
parent = [0] * (n + 1)

# 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

def bfs(start, visited):
    q = deque()
    q.append(start)
    visited[start] = 1
    
    while q:
        v = q.popleft()
        print(v)
        for i in range(1, n + 1):
            if visited[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited[i] = v

def dfs(depth, visited, parent):
    for value in graph[depth]:
        if visited[value] == 0:
            visited[value] = depth
            dfs(value, visited, parent)
    
    # for i in range(1, n + 1):
    #     if visited[i] == 0 and graph[depth][i] == 1:
    #         parent[i] = depth
    #         dfs(i, visited, parent)
    #     pass

# bfs(1, visited)
# for i in visited[2:]:
#     print(i)
dfs(1, visited2, parent)
for i in visited2[2:]:
    print(i)
