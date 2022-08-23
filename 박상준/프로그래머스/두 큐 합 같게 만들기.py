"""
 *packageName    : 
 * fileName       : 두 큐 합 같게 만들기
 * author         : ipeac
 * date           : 2022-08-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-21        ipeac       최초 생성
 """
from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    answer = 0
    q_sum1 = sum(queue1)
    q_sum2 = sum(queue2)
    for i in range(len(queue1) * 3 + 1):
        if q_sum1 == q_sum2:
            return answer
        if q_sum1 > q_sum2:
            num = queue1.popleft()
            queue2.append(num)
            answer += 1
            q_sum1 -= num
            q_sum2 += num
        elif q_sum2 > q_sum1:
            num = queue2.popleft()
            queue1.append(num)
            answer += 1
            q_sum1 += num
            q_sum2 -= num
    
    answer = -1
    return answer


# solution([3, 2, 7, 2], [4, 6, 5, 1])
# print("==========================================")
# solution([1, 2, 1, 2], [1, 10, 1, 2])
# print("==========================================")
solution([1, 1], [1, 5])
print("==========================================")
