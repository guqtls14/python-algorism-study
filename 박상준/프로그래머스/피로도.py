"""
 *packageName    : 
 * fileName       : 피로도
 * author         : ipeac
 * date           : 2022-08-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-18        ipeac       최초 생성
 """
from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for i in permutations(dungeons):
        tmp = 0
        v = k
        for line in i:
            if v < line[0]:
                break
            v -= line[1]
            tmp += 1
        answer = tmp if answer < tmp else answer
    
    return answer

print(solution(80, [[80, 20], [50, 40], [30, 10]]))
