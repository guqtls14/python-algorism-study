"""
 *packageName    : 
 * fileName       : 2075_N번째 큰 수_S2
 * author         : jihye94
 * date           : 2022-07-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-21        jihye94       최초 생성
 """
import heapq

heap = []
n = int(input())

for _ in range(n):
    numbers = map(int, input().split())
    for number in numbers:
        if len(heap) < n:  # heap의 크기를 n개로 유지
            heapq.heappush(heap, number)
            print("heap : %s " % heap)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
                print("heap : %s " % heap)
print(heap[0])
