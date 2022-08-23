"""
 *packageName    : 
 * fileName       : 3번
 * author         : ipeac
 * date           : 2022-08-22
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-22        ipeac       최초 생성
 """
from collections import deque


def solution(order):
    answer = 0
    n = len(order)
    main = deque([num for num in range(1, n + 1)])  # queue 처럼
    print(f"main : {main}")
    sub = []  # stack 처럼
    
    for i, required_box in enumerate(order):
        if sub and sub[-1] == required_box:
            sub.pop()
            answer += 1
        else:
            if not main:
                break
            while main:
                box = main.popleft()
                if box == required_box:
                    answer += 1
                    break
                else:
                    sub.append(box)
    
    print(f"answer : {answer}")
    return answer


solution([4, 3, 1, 2, 5])
