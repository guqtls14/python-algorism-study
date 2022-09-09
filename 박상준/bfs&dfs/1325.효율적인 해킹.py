"""
 *packageName    : 
 * fileName       : 1325.효율적인 해킹
 * author         : qkrtkdwns3410
 * date           : 2022-09-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-08        qkrtkdwns3410       최초 생성
 """
import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

def bfs(start):
    visited = [0] * (n + 1)
    q = deque()
    q.append(start)
    visited[start] = 1
    cnt = 1
    while q:
        x = q.popleft()
        for j in u[x]:
            if visited[j] == 0:
                visited[j] = 1
                q.append(j)
                cnt += 1
    return cnt

maax = []
max_cnt = -1
# n ; 컴퓨터 수 ; m;  신뢰 수
# 양방향
n, m, = map(int, input().split())
u = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    u[b].append(a)

for i in range(1, n + 1):
    res = bfs(i)
    maax.append([i, res])
    max_cnt = res if max_cnt < res else max_cnt
for i, v in maax:
    if max_cnt == v:
        print(i + " ")
