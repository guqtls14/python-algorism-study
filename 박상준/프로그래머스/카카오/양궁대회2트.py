"""
 *packageName    : 
 * fileName       : 양궁대회2트
 * author         : ipeac
 * date           : 2022-09-13
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-13        ipeac       최초 생성
 """
from itertools import combinations_with_replacement


def solution(n, info):
    answer = [-1]
    max_gap = -1  # 점수 차
    
    for combi in combinations_with_replacement(range(11), n):  # 중복 조합으로 0~10점까지 n개 뽑기
        print("==========================================")
        print(f"combi : {combi}")
        info2 = [0] * 11  # 라이언의 과녁 점수
        
        for i in combi:  # combi에 해당하는 화살들을 라이언의 과녁 점수에 넣기
            print(f"i : {i}")
            info2[10 - i] += 1
        apeach, lion = 0, 0
        print(f"info2 : {info2}")
        for idx in range(11):
            
            if info[idx] == info2[idx] == 0:  # 라이언과 어피치 모두 한번도 화살을 맞히지 못한 경우
                continue
            elif info[idx] >= info2[idx]:  # 어피치가 라이언이 쏜 화살수 이상
                apeach += 10 - idx
            elif info[idx] < info2[idx]:  # 라이언이 어차피 보다 많은 수의 화살 맞힌 경우
                lion += 10 - idx
        if lion > apeach:  # 라이언이 점수가 더 높음
            gap = lion - apeach
            if gap > max_gap:
                max_gap = gap
                answer = info2
    return answer


solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
# solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1])
# solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3])
