"""
 *packageName    : 
 * fileName       : [2019카카오]후보키
 * author         : qkrtkdwns3410
 * date           : 2022-08-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-24        qkrtkdwns3410       최초 생성
 """
from itertools import combinations as cb


def solution(relation):
    print(f"relation : {relation}")
    answer = 0
    row = len(relation)
    col = len(relation[0])
    # 가능한 속성의 모든 인덱스 조합
    combi = []
    for i in range(1, col + 1):
        combi.extend(cb(range(col), i))
    print(f"combi : {combi}")
    
    # 유일성 체크
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        
        if len(set(tmp)) == row:  # 유일성 만족
            put = True
            for x in unique:  # 유니크의 튜플이 combi안의 부분집합이라면 당연히 유니크에 추가하면 안됨.
                if set(x).issubset(set(i)):
                    put = False
                    break
            if put:
                print(f"i : {i}")
                unique.append(i)
    return len(unique)


solution(
    [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])
