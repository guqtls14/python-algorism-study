"""
 *packageName    : 
 * fileName       : 10819.차이를 최대로(2)
 * author         : ipeac
 * date           : 2022-09-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-29        ipeac       최초 생성
 """
from itertools import permutations

n = int(input())
a = list(map(int, input().split()))
answer = -1e9
# 다음 식의 최댓값을 구하는 프로그램
for combi in permutations(a, n):
    new_a = 0
    for i in range(0, n - 1):
        new_a += abs(combi[i] - combi[i + 1])
    answer = answer if answer > new_a else new_a
print(answer)
