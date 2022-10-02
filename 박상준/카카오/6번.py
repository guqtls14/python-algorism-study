"""
 *packageName    : 
 * fileName       : 6번
 * author         : ipeac
 * date           : 2022-09-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-24        ipeac       최초 생성
 """
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# n 세로 m 가로 x ,y : 시작점 r c 도착점 k 이동거리
def solution(n, m, x, y, r, c, k):
    answer = ''
    x -= 1
    y -= 1
    r -= 1
    c -= 1
    
    def bfs(x, y, answer):
        visited = [[0] * m for _ in range(n)]
        q = deque()
        q.append((x, y, answer))
        visited[x][y] = 1
        
        while q:
            xx, yy, answer = q.popleft()
            if xx == n - 1 and yy == m - 1:
                return answer
            
            for i in range(4):
                x_move = dx[i]
                y_move = dy[i]
                nx, ny = xx + dx[i], yy + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                    
                    if x_move == 0 and y_move == 1:
                        answer += 'r'
                    elif x_move == 0 and y_move == -1:
                        answer += 'l'
                    elif x_move == -1 and y_move == 0:
                        answer += 'd'
                    elif x_move == 1 and y_move == 0:
                        answer += 'u'
                    
                    visited[nx][ny] = 1
                    grid[nx][ny] = min(grid[nx][ny], grid[x][y] + 1)
                    q.append((nx, ny, answer))
        
        return answer
    
    grid = [[0] * m for _ in range(n)]
    print(bfs(x, y, answer))
    return grid[r][c]

print(solution(3, 4, 2, 3, 3, 1, 5))
# print(solution(2, 2, 1, 1, 2, 2, 2))
# print(solution(3, 3, 1, 2, 3, 3, 4))
