"""
 *packageName    : 
 * fileName       : 네트워크
 * author         : ipeac
 * date           : 2022-10-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-11        ipeac       최초 생성
 """
from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def bfs(com):
        visited[com] = 1
        q = deque()
        q.append(com)
        
        while q:
            x = q.popleft()
            for inner in range(n):
                if computers[x][inner] == 1 and visited[inner] == 0:
                    q.append(inner)
                    visited[inner] = 1
    
    for com in range(n):
        if visited[com] == 0:
            bfs(com)
            answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
