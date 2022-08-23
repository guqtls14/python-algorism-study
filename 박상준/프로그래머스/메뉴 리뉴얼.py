"""
 *packageName    : 
 * fileName       : 메뉴 리뉴얼
 * author         : ipeac
 * date           : 2022-08-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-23        ipeac       최초 생성
 """
from collections import Counter
from itertools import combinations


def solution(orders, course):
    print(f"orders : {orders}")
    print(f"course : {course}")
    answer = []
    
    for i in course:
        temp = []
        for menu in orders:
            for li in combinations(menu, i):
                res = ''.join(sorted(li))
                temp.append(res)
            print(f"temp : {temp}")
        common = Counter(temp).most_common()
        print(f"common : {common}")
        answer += [menu for menu, cnt in common if cnt > 1 and cnt == common[0][1]]
        print(f"answer : {answer}")
    return answer


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
