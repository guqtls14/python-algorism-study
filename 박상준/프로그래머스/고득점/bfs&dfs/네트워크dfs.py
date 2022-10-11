"""
 *packageName    : 
 * fileName       : 네트워크dfs
 * author         : ipeac
 * date           : 2022-10-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-11        ipeac       최초 생성
 """

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def dfs(com):
        visited[com] = 1
        
        for i in range(n):
            if computers[com][i] == 1 and visited[i] == 0:
                visited[i] = 1
                dfs(i)
        
        pass
    
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer += 1
    
    return answer

# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
