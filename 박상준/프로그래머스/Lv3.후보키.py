"""
 *packageName    : 
 * fileName       : Lv3.후보키
 * author         : ipeac
 * date           : 2022-08-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-18        ipeac       최초 생성
 """
from itertools import combinations


def solution(relation):
    print("relation : %s " % relation)
    
    row = len(relation)
    col = len(relation[0])
    # 가능한 속성의 모든 인덱스 조합
    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col), i))
    print("combi : %s " % combi)
    
    # 유일성
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        print("tmp : %s " % tmp)
        
        if len(set(tmp)) == row:  # 유일성 만족
            put = True
            for x in unique:
                # 유니크의 튜플이 combi안의
                if set(x).issubset(set(i)):
                    put = False
                    break
            if put:
                unique.append(i)


solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"],
          ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])
