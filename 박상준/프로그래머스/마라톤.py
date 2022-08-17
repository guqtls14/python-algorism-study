"""
 *packageName    : 
 * fileName       : 마라톤
 * author         : ipeac
 * date           : 2022-08-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-17        ipeac       최초 생성
 """
from collections import Counter


def solution(participant, completion):
    answer = ''
    print("participant : %s " % participant)
    print("completion : %s " % completion)
    
    item = Counter(participant) - Counter(completion)
    for value in item.keys():
        return value


solution(["leo", "kiki", "eden"], ["eden", "kiki"])
print("==========================================")
solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
print("==========================================")
solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
print("==========================================")
