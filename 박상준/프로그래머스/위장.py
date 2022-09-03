"""
 *packageName    : 
 * fileName       : 위장
 * author         : qkrtkdwns3410
 * date           : 2022-09-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-03        qkrtkdwns3410       최초 생성
 """
from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    for value in clothes:
        dic[value[1]] += 1
    print(f"dic : {dic}")
    counter = [counts + 1 for counts in dic.values()]
    
    for value in counter:
        answer *= value
    return answer - 1

# print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
# print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["yellow_hat", "headgear"], ["yellow_hat", "ehad"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
