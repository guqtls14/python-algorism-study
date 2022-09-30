"""
 *packageName    : 
 * fileName       : 2667.단지번호붙이기(2)
 * author         : ipeac
 * date           : 2022-09-30
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-30        ipeac       최초 생성
 """
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
gg = [list(map(int, input())) for _ in range(n)]
# print(f"gg : {gg}")
# gg = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]
visited = [[0] * n for _ in range(n)]

count_ans = []

def bfs(i, j):
    q = deque()
    q.append([i, j])
    cnt = 1
    visited[i][j] = 1
    
    while q:
        x, y = q.popleft()
        for xx, yy, in zip(dx, dy):
            nx = xx + x
            ny = yy + y
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and gg[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = 1
                cnt += 1
                pass
    return cnt

for i in range(n):
    for j in range(n):
        if gg[i][j] == 1 and not visited[i][j]:
            count_ans.append(bfs(i, j))
print(len(count_ans))
for i in sorted(count_ans):
    print(i)
