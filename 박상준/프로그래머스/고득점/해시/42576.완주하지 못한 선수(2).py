"""
 *packageName    : 
 * fileName       : 42576.완주하지 못한 선수(2)
 * author         : ipeac
 * date           : 2022-10-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-03        ipeac       최초 생성
 """
from collections import Counter

def solution(participant, completion):
    answer = ''
    counter_a = Counter(participant)
    print(f"counter_a : {counter_a}")
    
    counter_b = Counter(completion)
    print(f"counter_b : {counter_b}")
    
    count = counter_a - counter_b
    print(f"count : {count}")
    
    for name in count.keys():
        answer = name
    return answer

# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
