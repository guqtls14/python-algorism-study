"""
 *packageName    : 
 * fileName       : 1845.폰켓몬
 * author         : ipeac
 * date           : 2022-10-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-03        ipeac       최초 생성
 """
from itertools import permutations

def solution(nums):
    answer = 0
    check = len(nums) // 2
    
    nums_set = set(nums)
    
    if check >= len(nums_set):
        answer = len(nums_set)
    else:
        answer = check
    
    return answer

# print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
# print(solution([3, 3, 3, 2, 2, 2]))
