"""
 *packageName    : 
 * fileName       : 10971.외판원 순회2
 * author         : ipeac
 * date           : 2022-10-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-02        ipeac       최초 생성
 """
# n = int(input())
import sys

n = 4
# 도시간 이동 비용.
# w = [list(map(int, input().split())) for _ in range(n)]
# print(f"w : {w}")
w = [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]
min_size = sys.maxsize

def dfs(start, next, value, visited):  # 시작도시번호, 다음도시번호, 비용, 방문도시
    global min_size
    
    if len(visited) == n:  # 만약 방문한 도시가 입력받은 도시의 개수라면 -> 마지막 도시까지 다 들른경우
        if w[next][start] != 0:  # 마지막 도시에서 출발 도시로 가는 비용이 0이 아니라면(즉 , 갈수있다면)
            min_size = min(min_size, value + w[next][start])
        return
    
    for i in range(n):  # 도시의 개수 만큼 반복문을 돈다.
        # 만약 현재 도시에서 갈수있는 도시의 비용이 0이 아니고,
        # 이미 방문한 도시가 아니며
        # 그 비용값이 저장되어 있는 최소값보다 작다면
        if w[next][i] != 0 and i not in visited and value < min_size:
            visited.append(i)
            dfs(start, i, value + w[next][i], visited)
            visited.pop()

# 도시마다(0~3) 출발점을 지정
for i in range(n):
    dfs(i, i, 0, [i])
