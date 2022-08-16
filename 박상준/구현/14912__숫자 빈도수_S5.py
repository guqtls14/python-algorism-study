"""
 *packageName    : 
 * fileName       : 14912__숫자 빈도수_S5
 * author         : qkrtkdwns3410
 * date           : 2022-08-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-16        qkrtkdwns3410       최초 생성
 """

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solution(n, find_n):
    print("==========================================")
    graph = [list([0] * n) for _ in range(n)]
    print("map : %s " % graph)
    print("==========================================")
    
    row, col = 0, 0
    direction = 0
    
    cnt = n * n
    graph[0][0] = n * n
    cnt -= 1
    
    # 방향 전환및 숫자 채워넣기
    while cnt > 0:
        nx, ny = row + dx[direction], col + dy[direction]
        if nx >= 0 and ny >= 0 and graph[nx][ny] == 0:


solution(7, 35)
print("==========================================")
