"""
 *packageName    : 
 * fileName       : 게임 맵 최단거리
 * author         : qkrtkdwns3410
 * date           : 2022-09-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-01        qkrtkdwns3410       최초 생성
 """
#       오른 왼 위 아래
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(map):
    distance = [[0] * 5 for _ in range(5)]
    visited = [[False] * 5 for _ in range(5)]
    visited[0][0] = True
    q = deque()
    
    q.append([0, 0])
    
    while q:
        x, y, = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            print(f"nx,ny : {nx, ny}")
            if 0 <= nx < 5 and 0 <= ny < 5 and map[nx][ny] == 1:
                if not visited[nx][ny]:
                    print(f"nx, ny : {nx, ny}")
                    distance[nx][ny] = distance[x][y] + 1
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return distance

# 0 검은색 1 : 길
def solution(maps):
    answer = 0
    
    bfs(maps)
    
    return answer

print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
# print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
