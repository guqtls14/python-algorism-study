"""
 *packageName    : 
 * fileName       : 14712.넴모넴모(Easy)
 * author         : ipeac
 * date           : 2022-10-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-01        ipeac       최초 생성
 """
n, m = 2, 2  # x축 y축
# 넴모가 올라간 격자 판
graph = [[0 for _ in range(m)] for _ in range(n)]

# 격자판 탐색 - node는 넴모를 놓는 위치
def dfs(x, y):
    # 경우의 수 세기
    count = 0
    
    # 열이 격자판을 넘어가면 행을 하나 증가
    if y >= m:
        x += 1
        y = 0
    # 행을 증가했는데 격자판을 넘어간다면 전부 탐색한 것이다. - 탐색 종료
    if x >= n:
        return 0
    
    # 넴모를 놓아도 터트릴수 없는 위치라면 놓고, 다음 경우 탐색 - 3개중 한칸이라도 0이면 놓을 수 있다.
    if graph[x][y - 1] == 0 or graph[x - 1][y - 1] == 0 or graph[x - 1][y] == 0:
        # 넴모를 놓는다.
        graph[x][y] = 1
        # 넴모를 놓은 상태에서 재귀를 이용해서 다음 경우를 탐색하고, 그 결과에 현재 놓은 결과를 더해서 넣어준다.
        count += dfs(x, y + 1) + 1
        # 다음 탐색을 위하여 놓았던 네모를 다시 빈칸으로
        graph[x][y] = 0
    
    count += dfs(x, y + 1) + 1
    return count

print(dfs(0, 0))
