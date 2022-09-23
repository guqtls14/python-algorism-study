"""
 *packageName    : 
 * fileName       : 2961.도영이가 만든 맛있는 음식
 * author         : ipeac
 * date           : 2022-09-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-12        ipeac       최초 생성
 """
from itertools import combinations

n = int(input())
n_arr = [list(map(int, input().split())) for _ in range(n)]

min_diff = float('inf')

for i in range(1, n + 1):
    for j in combinations(n_arr, i):
        s = 1  # 신맛
        ss = 0  # 쓴맛
        for a, b in j:
            s *= a
            ss += b
        diff = abs(ss - s)
        min_diff = diff if min_diff > diff else min_diff
print(min_diff)
