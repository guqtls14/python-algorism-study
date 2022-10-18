"""
 *packageName    : 
 * fileName       : 금 채굴하기
 * author         : ipeac
 * date           : 2022-10-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-18        ipeac       최초 생성
 """
from collections import deque

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
# n, m, = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
# print(f"n,m = {n, m}")
# print(f"graph = {graph}")

n, m = (5, 5)
graph = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0]]

def get_area(k):
    return k * k + (k + 1) * (k + 1)

# 주어진 k에 대하여 채굴 가능한 금의 개수를 반환합니다.
def get_num_of_gold(row, col, k):
    return sum([graph[i][j] for i in range(n) for j in range(n) if abs(row - i) + abs(col - j) <= k])

max_gold = 0

for row in range(n):
    for col in range(n):
        for k in range(2 * (n - 1) + 1):
            num_of_gold = get_num_of_gold(row, col, k)
            
            # 손해를 보지 않고 채굴하기 위하여
            if num_of_gold * m >= get_num_of_gold(row, col, k):
                max_gold = max(max_gold, num_of_gold)
print(max_gold)
