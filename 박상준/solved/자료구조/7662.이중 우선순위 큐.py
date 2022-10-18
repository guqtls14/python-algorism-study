"""
 *packageName    : 
 * fileName       : 7662.이중 우선순위 큐
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

T = int(input())
for i in range(T):
    q = []
    k = int(input())
    for j in range(k):
        stmt, n = map(str, input().split())
        n = int(n)
        
        if len(q) == 0 and stmt == 'D':
            continue
        
        if stmt == 'I':
            heapq.heappush(q, n)
        
        elif stmt == 'D' and n == -1:
            heapq.heappop(q)
        
        elif stmt == 'D' and n == 1:
            q.remove(heapq.nlargest(1, q)[0])
    
    if len(q) == 0:
        print('EMPTY')
    else:
        print(heapq.nlargest(1, q)[0], end=" ")
        print(heapq.heappop(q))
