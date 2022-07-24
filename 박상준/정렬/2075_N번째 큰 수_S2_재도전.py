"""
 *packageName    : 
 * fileName       : 2075_N번째 큰 수_S2_재도전
 * author         : jihye94
 * date           : 2022-07-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-23        jihye94       최초 생성
 """
import heapq

n = int(input())

q = []

for i in range(n):
    line = map(int, input().split())
    for value in line:
        if len(q) < n:
            heapq.heappush(q, value)
        else:
            if q[0] < value:
                heapq.heappushpop(q, value)

print(q[0])
