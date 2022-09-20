"""
 *packageName    : 
 * fileName       : 2798.블랙잭
 * author         : qkrtkdwns3410
 * date           : 2022-09-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-18        qkrtkdwns3410       최초 생성
 """
# 카드의 개수 n 과 m
from itertools import combinations

# n, m = 5, 21
n, m = map(int, input().split())
# 둘째줄 카드에 쓰여있는 수
# cards = [5, 6, 7, 8, 9]
cards = list(map(int, input().split()))
max_num = float('-inf')
for combi in combinations(cards, 3):
    value = sum(combi)
    if value <= m:
        max_num = value if max_num < value else max_num
print(max_num)
