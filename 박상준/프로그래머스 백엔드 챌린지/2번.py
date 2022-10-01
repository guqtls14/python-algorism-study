"""
 *packageName    : 
 * fileName       : 2번
 * author         : ipeac
 * date           : 2022-10-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-01        ipeac       최초 생성
 """
from itertools import permutations

number_list = [[0, 6], [1, 2], [2, 5], [3, 5], [4, 4], [5, 5], [6, 6], [7, 3], [8, 7], [9, 6]]
arr = set()

def solution(k):
    # k개의 성냥개비로 만들수있는 숫자
    answer = set()
    
    for i in range(len(number_list)):
        for combi in permutations(number_list, i):
            sum_of = 0
            num = ''
            for ll in combi:
                num += str(ll[0])
                sum_of += ll[1]
            if sum_of <= k and num != '':
                arr.add(int(num))
    return len(arr)

print(solution(5))
# print(solution(6))
# print(solution(11))
# print(solution(1))
