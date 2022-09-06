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
visited = []

def bfs(graph, start, visited):
    pass

def dfs(graph, start, visited):
    pass

def solution(n, m, v, node):
    visited = [0] * (n + 1)
    
    graph = [[] for _ in range(n + 1)]
    for node in node:
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])
    print(f"graph : {graph}")
    
    # bfs(graph, 1, visited)
    dfs(graph, 1, visited)

solution(n=4, m=5, v=1, node=[[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]])
