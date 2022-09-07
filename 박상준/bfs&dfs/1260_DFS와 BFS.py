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

input = sys.stdin.readline

def bfs(graph, start, visited):
    pass

def dfs(graph, start, visited):
    pass

# n 정점의 개수 m 간선의 개수 탐색을 시작할 정점의 번호 v node : 간선이 연결하는 두 정점의 번호
def solution(n, m, v, node):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    visited_list1 = [0] * (n + 1)
    visitied_list2 = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = graph[b][a] = 1
    pass

solution(n=4, m=5, v=1, node=[[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]])
