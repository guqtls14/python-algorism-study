"""
 *packageName    : 
 * fileName       : 위장
 * author         : ipeac
 * date           : 2022-10-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-10        ipeac       최초 생성
 """
from collections import defaultdict

def solution(clothes):
    dic = defaultdict(int)
    for name, kind in clothes:
        dic[kind] += 1
    ans = 1
    for value in dic.values():
        ans *= value + 1
    return ans - 1

# print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
