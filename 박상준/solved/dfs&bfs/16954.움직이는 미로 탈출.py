"""
 *packageName    : 
 * fileName       : 16954.움직이는 미로 탈출
 * author         : ipeac
 * date           : 2022-10-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-06        ipeac       최초 생성
 """
from collections import deque

MAX = 8
direction = [[0, 0], [0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [1, -1], [1, 1], [-1, 1]]
graph = [list(input()) for _ in range(MAX)]
visited = [[0] * MAX for _ in range(MAX)]

dq = deque([[0, 7, 0]])  # y x 버틴 시간

answer = 0
while dq:
    cur = dq.popleft()
    
    for dx, dy in direction:  # 9방향 이동
        nx = cur[0] + dx  # 가로 좌표
        ny = cur[1] + dy  # 세로 좌표
        
        if cur[1] == 0 or cur[2] == 7:  # 세로 좌표가 0에 닿았거나, 버틴 시간이 7 턴 이라면 가능한 조합임.
            answer = 1
            break
        
        if 0 > nx or 0 > ny or MAX <= nx or MAX <= ny: continue
        
        if ny - cur[2] < 0:  # 움직인 세로좌표 보다 버틴 시간이 더 크다면 # 이 다 지나간 경우임 무조건 가능
            dq.clear()
            answer = 1
            break
        
        if visited[ny][nx] >= cur[2] + 1:  # 버틴 시간+1 보다 visit.. 가 더 크다면 패스
            continue
        
        if graph[ny - cur[2]][nx] == '#': ㅔ
        continue
    
    if graph[ny - (cur[2] + 1)][nx] == '#':
        continue
    
    dq.append([nx, ny, cur[2] + 1])
    
    visited[ny][nx] = cur[2] + 1

print(answer)
