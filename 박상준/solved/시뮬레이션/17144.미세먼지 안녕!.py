"""
 *packageName    : 
 * fileName       : 17144.미세먼지 안녕!
 * author         : ipeac
 * date           : 2022-10-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-03        ipeac       최초 생성
 """
import copy
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

R, C, T = 7, 8, 1
# A = [list(map(int, input().split())) for _ in range(R)]
A = [[0, 0, 0, 0, 0, 0, 0, 9], [0, 0, 0, 0, 3, 0, 0, 8], [-1, 0, 5, 0, 0, 0, 22, 0], [-1, 8, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 10, 43, 0], [0, 0, 5, 0, 15, 0, 0, 0], [0, 0, 40, 0, 0, 0, 20, 0]]

# 공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다.
# -1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.
# , T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양을 구해보자.

def bfs(i, j):
    new_A = copy.deepcopy(A)
    visited = [[0] * C for _ in range(R)]
    
    while q:
        x, y = q.popleft()
        cnt = 0  # 방향 카운트
        check_arr = deque()  # 방향정보를 담습니다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0 and A[nx][ny] != -1:
                cnt += 1
                check_arr.append([nx, ny])
                visited[nx][ny] = 1
        # 방향에 맞는 먼지 계산
        for x, y in check_arr:
            A[]
            pass

# 0행 0열에서만 먹는것인가?
for i in range(R):
    for j in range(C):
        if A[i][j] != 0 and A[i][j] != -1:
            bfs(i, j)
