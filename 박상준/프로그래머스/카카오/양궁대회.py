"""
 *packageName    : 
 * fileName       : 양궁대회
 * author         : ipeac
 * date           : 2022-08-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-28        ipeac       최초 생성
 """
from itertools import combinations_with_replacement


def solution(n, info):
    answer = [-1]
    max_gap = -1  # 점수 차
    for combi in combinations_with_replacement(range(11), n):
        info2 = [0] * 11
        
        for i in combi:  # combi에 해당하는 화살들을 라이언 과녁 점수에 넣기
            info2[10 - i] += 1
        
        apeach, lion = 0, 0
        
        for idx in range(11):
            if info[idx] == info2[idx] == 0:
                continue
            elif info[idx] >= info2[idx]:
                apeach += 10 - idx
            else:
                lion += 10 - idx
        
        if lion > apeach:
            gap = lion - apeach
            if gap > max_gap:
                max_gap = gap
                answer = info2
    return answer


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
# print("==========================================")
# print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
# print("==========================================")
# print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
# print("=========================================")
# print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
