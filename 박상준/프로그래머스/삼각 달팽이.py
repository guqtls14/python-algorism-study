"""
 *packageName    : 
 * fileName       : 삼각 달팽이
 * author         : ipeac
 * date           : 2022-09-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-05        ipeac       최초 생성
 """
import pprint

def solution(n):  # 4
    answer = []
    graph = [list([0] * i) for i in range(1, n + 1)]
    r = len(graph)
    x, y = -1, 0  # 좌표 초기화 > 처음 시작은 아래로 내려감
    num = 1  # 4 3 2 1
    for i in range(n):  # 0 1 2 3
        for j in range(i, n):  # 0123 123 23 3
            if i % 3 == 0:  # 아래로
                x += 1
                pass
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                y -= 1
                x -= 1
            graph[x][y] = num
            num += 1
    for value in graph:
        for i in value:
            answer.append(i)
    return answer

print(solution(4))
# print(solution(5))  # [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9]
# print(solution(6))
