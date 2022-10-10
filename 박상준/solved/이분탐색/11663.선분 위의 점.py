"""
 *packageName    : 
 * fileName       : 11663.선분 위의 점
 * author         : ipeac
 * date           : 2022-10-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-07        ipeac       최초 생성
 """
import bisect

n, m = map(int, input().split())
lines = list(map(int, input().split()))
line_node = []
for i in range(m):
    a, b = map(int, input().split())
    line_node.append([a, b])
lines.sort()

for node in line_node:
    min_node = node[0]
    max_node = node[1]
    print(bisect.bisect_right(lines, max_node) - bisect.bisect_left(lines, min_node))
