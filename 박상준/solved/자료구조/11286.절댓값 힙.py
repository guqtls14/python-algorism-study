"""
 *packageName    : 
 * fileName       : 11286.절댓값 힙
 * author         : ipeac
 * date           : 2022-10-15
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-15        ipeac       최초 생성
 """
import heapq
import sys

input = sys.stdin.readline

n = int(input())
info = []
for i in range(n):
    x = int(input())
    # 배열에서 절댓값이 가장 작은 값을 출력 -> 그 값을 배열에서 제거
    if x == 0:
        if len(info) == 0:
            print(0)
            continue
        print(heapq.heappop(info)[1])
    else:  # 배열에 값추가
        heapq.heappush(info, (abs(x), x))
