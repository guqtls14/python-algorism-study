"""
 *packageName    : 
 * fileName       : Lv2.구명보트
 * author         : ipeac
 * date           : 2022-10-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-04        ipeac       최초 생성
 """
from collections import deque

def solution(people, limit):
    people.sort()
    # 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return
    cnt = 0
    a = []
    i = 0
    j = len(people) - 1
    while i <= j:
        cnt += 1
        if people[j] + people[i] <= limit:
            i += 1
        j -= 1
    
    return cnt

# print(solution([70, 50, 80, 50], 100))
# print(solution([50, 60, 40, 20, 30], 110))
print(solution([100, 500, 500, 900, 950], 1000))
# print(solution([70, 80, 50], 100))
