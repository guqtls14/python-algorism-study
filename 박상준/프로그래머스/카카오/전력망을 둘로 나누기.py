"""
 *packageName    : 
 * fileName       : 전력망을 둘로 나누기
 * author         : qkrtkdwns3410
 * date           : 2022-09-15
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-15        qkrtkdwns3410       최초 생성
 """
from collections import deque

def bfs(v, n, grid):
    cnt = 0
    
    q = deque()
    q.append(v)
    
    visited = [0 for _ in range(n + 1)]
    visited[v] = 1
    
    while q:
        v = q.popleft()
        
        for w in grid[v]:
            if not visited[w]:
                visited[w] = 1
                q.append(w)
                cnt += 1
    return cnt

def solution(n, wires):
    answer = float('inf')
    
    # 인접 리스트
    grid = [[] for _ in range(n + 1)]
    
    # 양방향 연결 그리드
    for i in range(n - 1):
        grid[wires[i][0]].append(wires[i][1])
        grid[wires[i][1]].append(wires[i][0])
    
    for i in range(n - 1):
        grid[wires[i][0]].remove(wires[i][1])
        grid[wires[i][1]].remove(wires[i][0])
        
        cnt_node1 = bfs(wires[i][0], n, grid)
        cnt_node2 = bfs(wires[i][1], n, grid)
        
        answer = min(answer, abs(cnt_node1 - cnt_node2))
        
        grid[wires[i][0]].append(wires[i][1])
        grid[wires[i][1]].append(wires[i][0])
    
    return answer

# solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]])
# print(solution(4, [[1, 2], [2, 3], [3, 4]]))
solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]])
