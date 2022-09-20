"""
 *packageName    : 
 * fileName       : 14502.연구소
 * author         : ipeac
 * date           : 2022-09-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-19        ipeac       최초 생성
 """
import copy
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
# n, m = 7, 7
#
grid = [list(map(int, input().split())) for _ in range(n)]


#
#
# grid = [[2, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 2, 0], [0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]


def bfs():
    q = deque()
    tmp_grid = copy.deepcopy(grid)

    for i in range(n):
        for j in range(m):
            if tmp_grid[i][j] == 2:  # 2의 좌표를 담는다.
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tmp_grid[nx][ny] == 0:
                tmp_grid[nx][ny] = 2
                q.append((nx, ny))

    global answer

    cnt = 0
    for i in range(n):
        cnt += tmp_grid[i].count(0)
    answer = max(answer, cnt)


def make_wall(cnt, start_row, start_col):
    if cnt == 3:
        bfs()
        return
    for i in range(start_row, n):
        for j in range(start_col, m):
            if grid[i][j] == 0:
                grid[i][j] = 1
                make_wall(cnt + 1, i, j + 1)
                grid[i][j] = 0
        start_col = 0


answer = 0
make_wall(0, 0, 0)
print(answer)
