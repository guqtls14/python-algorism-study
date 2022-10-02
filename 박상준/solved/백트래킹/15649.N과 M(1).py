"""
 *packageName    : 
 * fileName       : 15649.N과 M(1)
 * author         : ipeac
 * date           : 2022-10-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-01        ipeac       최초 생성
 """
from itertools import permutations

n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]

for combi in permutations(arr, m):
    print(*combi)
