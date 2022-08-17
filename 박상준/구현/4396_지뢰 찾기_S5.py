"""
 *packageName    : 
 * fileName       : 4396_지뢰 찾기_S5
 * author         : ipeac
 * date           : 2022-08-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-16        ipeac       최초 생성
 """
dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [-1, 1, 1, -1, 0, 1, -1, 0]

n = int(input())
mine_map = [list(map(str, input())) for _ in range(n)]
graph = [list(map(str, input())) for _ in range(n)]


def solution(n, mine_map, graph):
    print("==========================================")
    print("n : %s " % n)
    print("mine_map : %s " % mine_map)
    print("graph : %s " % graph)
    print("==========================================")
    
    mine_flag = False
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'x':
                if mine_map[i][j] == '*':
                    mine_flag = True
                    continue
                
                cnt = 0
                for k in range(8):
                    nx, ny = i + dx[k], j + dy[k]
                    # 근처 지뢰 파악
                    if n > nx >= 0 and n > ny >= 0 and mine_map[nx][ny] == '*':
                        cnt += 1
                graph[i][j] = str(cnt)
            print("graph : %s " % graph)
    
    # 만약 지뢰를 밟았다면
    if mine_flag:
        for i in range(n):
            for j in range(n):
                if mine_map[i][j] == '*':
                    graph[i][j] = '*'
    
    for line in graph:
        print(''.join(line))


solution(n, mine_map, graph)
print("==========================================")
