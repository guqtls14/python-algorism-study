"""
 *packageName    : 
 * fileName       : 보급로
 * author         : ipeac
 * date           : 2022-08-30
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-30        ipeac       최초 생성
 """
import pprint
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(graph, n):
    depth = [[float('inf')] * n for _ in range(n)]
    depth[0][0] = 0
    print(f"depth : {depth}")
    q = deque()
    q.append([0, 0])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if depth[nx][ny] > depth[x][y] + graph[nx][ny]:
                    depth[nx][ny] = depth[x][y] + graph[nx][ny]
                    q.append([nx, ny])
    
    return depth

def solution():
    TC = int(input())
    for tc in range(TC):
        n = int(input())
        graph = []
        for i in range(n):
            m = map(int, input())
            graph.append(list(m))
        
        depth_a = bfs(graph, n)
        
        print('#{} {}'.format(tc + 1, depth_a[n - 1][n - 1]))

solution()
