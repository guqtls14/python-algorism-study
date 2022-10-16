"""
 *packageName    : 
 * fileName       : 11286.절댓값 힙(2)
 * author         : ipeac
 * date           : 2022-10-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-16        ipeac       최초 생성
 """
import heapq
import sys

input = sys.stdin.readline

n = int(input())
infos = []
for i in range(n):
    infos.append(int(input()))
# print(f"n = {n}")
# print(f"infos = {infos}")
# n = 18
# infos = [1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0, 0, 0, 0, 0, 0]
q = []
for x in infos:
    # 배열에 x라는 값을 넣는 연산
    if x != 0:
        heapq.heappush(q, (abs(x), x))  # 절댓값, 원값
    # 배열에서 절댓값이 가장 작은 값을 출력 하고 그 값을 제거
    else:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
