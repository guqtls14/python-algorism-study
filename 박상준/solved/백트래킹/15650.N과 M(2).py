"""
 *packageName    : 
 * fileName       : 15650.N과 M(2)
 * author         : ipeac
 * date           : 2022-10-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-01        ipeac       최초 생성
 """
from itertools import combinations

n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]

for combi in combinations(arr, m):
    print(*combi)
