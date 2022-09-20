"""
 *packageName    : 
 * fileName       : 1987.알파벳
 * author         : qkrtkdwns3410
 * date           : 2022-09-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-20        qkrtkdwns3410       최초 생성
 """
from collections import defaultdict

dx = [0, 0, 1 - 1]
dy = [1, -1, 0, 0]

# 세로 r 가로 c
r, c = map(int, input().split())
dic = defaultdict(int)
grid = [list(map(str, input())) for _ in range(r)]
# grid = [['C', 'A', 'A', 'B'], ['A', 'D', 'C', 'B']]
# grid = []
for i in range(r):
    for j in range(c):
        dic[grid[i][j]] = 1


def dfs(i, j, cnt):
    global answer
    answer = cnt if answer < cnt else answer
    for x, y in zip(dx, dy):
        nx, ny = x + i, y + j
        if 0 <= nx < r and 0 <= ny < c and dic[grid[nx][ny]] == 1:
            dic[grid[nx][ny]] = 0
            dfs(nx, ny, cnt + 1)
            dic[grid[nx][ny]] = 1


answer = -1e9

dfs(0, 0, 1)
print(answer)
