"""
 *packageName    : 
 * fileName       : 1번
 * author         : ipeac
 * date           : 2022-10-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-01        ipeac       최초 생성
 """
from collections import deque

def solution(arr):
    answer = set()
    arr.sort(key=lambda x: len(str(x)))
    
    for value in arr:
        value = sorted(list(str(value)))
        tmp = ''
        for i in value:
            tmp += i
        answer.add(tmp)
    
    return len(answer)

print(solution([112, 1814, 121, 1481, 1184]))  # 2
print(solution([123, 456, 789, 321, 654, 987]))  # 3
print(solution([1, 2, 3, 1, 2, 3, 4]))  # 4
print(solution([123, 234, 213, 432, 234, 1234, 2341, 12345, 324]))  # 4
