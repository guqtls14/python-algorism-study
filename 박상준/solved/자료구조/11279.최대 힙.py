"""
 *packageName    : 
 * fileName       : 11279.최대 힙
 * author         : ipeac
 * date           : 2022-10-15
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-15        ipeac       최초 생성
 """
# n = int(input())
# print(f"n = {n}")
# info = list(int(input()) for _ in range(n))
# print(f"info = {info}")
import heapq
import sys

input = sys.stdin.readline
n = int(input())

info = []

for i in range(n):
    num = int(input())
    if num == 0:
        if len(info) == 0:
            print(0)
            continue
        
        max_value = - heapq.heappop(info)
        print(max_value)
    else:
        heapq.heappush(info, -num)
