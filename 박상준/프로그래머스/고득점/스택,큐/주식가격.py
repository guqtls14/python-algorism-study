"""
 *packageName    : 
 * fileName       : 주식가격
 * author         : ipeac
 * date           : 2022-10-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-10        ipeac       최초 생성
 """
from collections import deque

# 스택 큐
def solution(prices):
    q = deque(prices)
    answer = []
    
    while q:
        price = q.popleft()
        sec = 0
        for qu in q:
            sec += 1
            
            if price > qu:
                break
        answer.append(sec)
    return answer

print(solution([1, 2, 3, 4, 1]))
