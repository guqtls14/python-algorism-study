"""
 *packageName    : 
 * fileName       : 11660.구간 합 구하기 5
 * author         : qkrtkdwns3410
 * date           : 2022-09-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-17        qkrtkdwns3410       최초 생성
 """
import sys

input = sys.stdin.readline
# 표의 크기 n ; 합을 구해야 하는 횟수 m
n, m = map(int, input().split())
# grid = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
grid = [list(map(int, input().split())) for _ in range(n)]
input_me = [list(map(int, input().split())) for _ in range(m)]
# input_me = [[2, 2, 3, 4], [3, 4, 3, 4], [1, 1, 4, 4]]
prefix_arr = [[0] * (n + 1) for _ in range(n + 1)]
# 구간합 행렬을 만들어야함.
for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_arr[i][j] = prefix_arr[i - 1][j] + prefix_arr[i][j - 1] - prefix_arr[i - 1][j - 1] + grid[i - 1][
            j - 1]
for i in input_me:
    x1, y1, x2, y2 = map(int, i)
    print(prefix_arr[x2][y2] - prefix_arr[x2][y1 - 1] - prefix_arr[x1 - 1][y2] + prefix_arr[x1 - 1][y1 - 1])
