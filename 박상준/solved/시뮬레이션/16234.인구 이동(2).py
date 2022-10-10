"""
 *packageName    : 
 * fileName       : 16234.인구 이동(2)
 * author         : ipeac
 * date           : 2022-10-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-03        ipeac       최초 생성
 """
import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

input = sys.stdin.readline

N, L, R = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(N))

# 인구 이동이 며칠동안 발생하는지 첫째 줄에 입력한다.
# 인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.
def bfs(i, j, visited):
    total_population = 0
    total_size = 0
    total_index = deque()
    
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    total_population += A[i][j]
    total_size += 1
    total_index.append([i, j])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(A[nx][ny] - A[x][y]) <= R:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    total_size += 1
                    total_population += A[nx][ny]
                    total_index.append([nx, ny])
    
    if total_size >= 2:
        sum_if = total_population // total_size
        
        for line in total_index:
            x, y = map(int, line)
            A[x][y] = sum_if
        
        return total_population, total_size, total_index
    else:
        return -1, -1, []

day = 0
while True:
    max_size = -1
    visited = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                total_population, total_size, total_index = bfs(i, j, visited)
                max_size = max_size if max_size > total_size else total_size
    
    if max_size == -1:
        break
    day += 1
print(day)
