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
    row = len(map)
    col = len(map[0])
    
    answer = 0
    distance = [[0] * col for _ in range(row)]
    visited = [[False] * col for _ in range(row)]
    visited[0][0] = True
    q = deque()
    
    q.append([0, 0])
    
    while q:
        x, y, = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            print(f"nx,ny : {nx, ny}")
            if 0 <= nx < row and 0 <= ny < col and map[nx][ny] == 1:
                if not visited[nx][ny]:
                    print(f"nx, ny : {nx, ny}")
                    distance[nx][ny] = distance[x][y] + 1
                    visited[nx][ny] = True
                    q.append([nx, ny])
    answer = -1 if distance[row - 1][col - 1] == 0 else distance[row - 1][col - 1] + 1
    return answer

# 0 검은색 1 : 길
def solution(maps):
    return bfs(maps)

print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
print(solution([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))
