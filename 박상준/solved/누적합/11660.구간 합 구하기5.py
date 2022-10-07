"""
 *packageName    : 
 * fileName       : 11660.구간 합 구하기5
 * author         : ipeac
 * date           : 2022-10-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-07        ipeac       최초 생성
 """
import itertools
import pprint

# 표의 크기 N             합을 구해야 하는 횟수 M이 주어진다
# n, m = 4, 3
n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
input_me = [list(map(int, input().split())) for _ in range(m)]

prefix_arr = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_arr[i][j] = prefix_arr[i - 1][j] + prefix_arr[i][j - 1] - prefix_arr[i - 1][j - 1] + grid[i - 1][j - 1]
pprint.pprint(prefix_arr)
for i in input_me:
    x1, y1, x2, y2 = map(int, i)
    print(prefix_arr[x2][y2] - prefix_arr[x2][y1 - 1] - prefix_arr[x1 - 1][y2] + prefix_arr[x1 - 1][y1 - 1])
