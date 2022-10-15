"""
 *packageName    :
 * fileName       : 2075.N번째 큰 수
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

q = []

for i in range(n):
    line = list(map(int, input().split()))
    
    for value in line:
        if len(q) < n:
            heapq.heappush(q, value)
        else:
            if q[0] < value:
                heapq.heappushpop(q, value)  # q의 최솟값보다 큰 값을 넣고 최소값을 pop
print(q[0])
