"""
 *packageName    : 
 * fileName       : 2252.줄 세우기
 * author         : ipeac
 * date           : 2022-09-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-28        ipeac       최초 생성
 """
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
inDegree = [0 for _ in range(n + 1)]  # 진입차수
q = deque()
answer = []

for i in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    inDegree[b] += 1  # 진입차수 증가

for i in range(1, n + 1):
    if inDegree[i] == 0:  # 진입차수 0 이면 우선순위임. 큐에 담습니다.
        q.append(i)

while q:
    tmp = q.popleft()
    answer.append(tmp)
    
    for i in graph[tmp]:
        inDegree[i] -= 1  # 진입차수 순에 따라 큐에 담는다.
        if inDegree[i] == 0:
            q.append(i)

print(*answer)
