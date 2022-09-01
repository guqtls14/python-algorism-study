"""
 *packageName    : 
 * fileName       : [1차] 뉴스 클러스터링
 * author         : qkrtkdwns3410
 * date           : 2022-08-30
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-30        qkrtkdwns3410       최초 생성
 """
from collections import Counter

def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    str1_arr = [str1[i:i + 2] for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    str2_arr = [str2[i:i + 2] for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]
    
    counter1 = Counter(str1_arr)
    counter2 = Counter(str2_arr)
    
    # 교집합
    intersections = list((counter1 & counter2).elements())
    # 합집합
    unions = list((counter1 | counter2).elements())
    
    if len(unions) == 0:
        return 65536
    else:
        return int(len(intersections) / len(unions) * 65536)

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
