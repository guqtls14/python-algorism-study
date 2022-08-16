"""
 *packageName    : 
 * fileName       : 4번
 * author         : jihye94
 * date           : 2022-08-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-06        jihye94       최초 생성
 """
import collections


def solution(invitationPairs):
    print("invitationPairs : %s " % invitationPairs)
    diction = collections.defaultdict(int)
    
    for item in invitationPairs:
        diction[item[0]] += 0
    answer = []
    
    return answer


solution([[1, 2], [2, 3], [2, 4], [2, 5], [5, 6], [5, 7], [6, 8], [2, 9]])
print("==========================================")
solution([[1, 2], [1, 3], [3, 4], [4, 5], [4, 6], [4, 7]])
print("==========================================")
solution([[1, 2], [3, 4]])
