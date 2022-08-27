"""
 *packageName    : 
 * fileName       : [카카오 인턴십]거리두기 확인하기
 * author         : ipeac
 * date           : 2022-08-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-24        ipeac       최초 생성
 """
import pprint
from collections import deque


def bfs(p):
    start = []
    
    for i in range(5):  # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    for s in start:
        queue = deque([s])
        visited = [[0] * 5 for _ in range(5)]  # 방문자 처리 리스트
        distance = [[0] * 5 for _ in range(5)]  # 방문 경로 체크
        visited[s[0]][s[1]] = 1
        
        while queue:
            x, y = queue.popleft()
            
            dx = [0, 0, -1, 1]
            dy = [-1, 1, 0, 0]
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0:
                    if p[nx][ny] == 'O':
                        visited[nx][ny] = 1
                        queue.append([nx, ny])
                        distance[nx][ny] = distance[x][y] + 1
                    
                    if p[nx][ny] == 'P' and distance[x][y] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    
    for i in places:
        answer.append(bfs(i))
    
    return answer


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
