"""
 *packageName    : 
 * fileName       : 10819.차이를 최대로
 * author         : ipeac
 * date           : 2022-09-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-16        ipeac       최초 생성
 """
from itertools import permutations

# n = 6
# a = [20, 1, 15, 8, 4, 10]

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
answer = 0

for i in permutations(a, len(a)):
    tmp = 0
    for index in range(len(i) - 1):
        tmp += abs(i[index] - i[index + 1])
    answer = answer if answer > tmp else tmp
print(answer)
