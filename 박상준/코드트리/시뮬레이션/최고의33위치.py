"""
 *packageName    : 
 * fileName       : 최고의33위치
 * author         : ipeac
 * date           : 2022-10-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-17        ipeac       최초 생성
 """
import sys

input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def calc_three(row, col, row_p, col_p):
    sum_value = 0
    for x in range(row, row_p + 1):
        for y in range(col, col_p + 1):
            sum_value += graph[x][y]
    return sum_value

max_value = 0

for row in range(n):
    for col in range(n):
        if row + 2 >= n or col + 2 >= n:
            continue
        else:
            value = calc_three(row, col, row + 2, col + 2)
        max_value = max(max_value, value)

print(max_value)
