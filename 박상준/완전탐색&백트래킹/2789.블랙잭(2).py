"""
 *packageName    : 
 * fileName       : 2789.블랙잭(2)
 * author         : ipeac
 * date           : 2022-09-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-29        ipeac       최초 생성
 """
from itertools import permutations

n, m = map(int, input().split())
# 카드 3장 고르는거임 목표수 m
cards = list(map(int, input().split()))
ans = 10e9
ans2 = 0
for combi in permutations(cards, 3):
    sum_of = sum(combi)
    if sum_of > m:
        continue
    tmp = abs(m - sum_of)
    
    if ans > tmp:
        ans = tmp
        ans2 = sum_of
print(ans2)
