"""
 *packageName    : 
 * fileName       : 전력망을 둘로 나누기
 * author         : ipeac
 * date           : 2022-10-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-11        ipeac       최초 생성
 """
from collections import deque

def solution(n, wires):
    answer = 1e9
    graph = [[] for _ in range(n + 1)]
    
    for i in range(len(wires)):
        graph[wires[i][0]].append(wires[i][1])
        graph[wires[i][1]].append(wires[i][0])
    print(f"graph : {graph}")
    
    def bfs(i):
        q = deque()
        q.append(i)
        visited[i] = 1
        cnt = 1
        while q:
            x = q.popleft()
            for k in graph[x]:
                if not visited[k]:
                    q.append(k)
                    visited[k] = 1
                    cnt += 1
        return cnt
    
    for i in range(len(wires)):
        visited = [0] * (n + 1)
        
        graph[wires[i][0]].remove(wires[i][1])
        graph[wires[i][1]].remove(wires[i][0])
        
        cnt1 = bfs(wires[i][0])
        cnt2 = bfs(wires[i][1])
        
        answer = min(answer, abs(cnt2 - cnt1))
        
        graph[wires[i][0]].append(wires[i][1])
        graph[wires[i][1]].append(wires[i][0])
    
    return answer

# print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
# print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
