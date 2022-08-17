"""
 *packageName    : 
 * fileName       : 1913_달팽이_S5
 * author         : ipeac
 * date           : 2022-08-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-16        ipeac       최초 생성
 """
import sys

input = sys.stdin.readline

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def solution(n, find_n):
    print("n : %s " % n)
    print("find_n : %s " % find_n)
    print("==========================================")
    
    graph = [list([0] * n) for _ in range(n)]
    print("graph : %s " % graph)
    print("==========================================")
    row, col = 0, 0
    result_x, result_y = 0, 0
    direction = 0
    cnt = n * n
    graph[0][0] = cnt
    cnt -= 1
    
    while cnt > 0:
        nx, ny = row + dx[direction], col + dy[direction]
        if n > nx >= 0 and n > ny >= 0 and graph[nx][ny] == 0:
            if cnt == find_n:
                result_x = nx
                result_y = ny
            graph[nx][ny] = cnt
            row = nx
            col = ny
            cnt -= 1
            pass
        else:
            if direction == 3:
                direction = 0
            else:
                
                direction += 1
    for line in graph:
        for value in line:
            print(value, end=" ")
        print()
    print(result_x + 1, result_y + 1)


solution(int(input()), int(input()))
print("==========================================")
