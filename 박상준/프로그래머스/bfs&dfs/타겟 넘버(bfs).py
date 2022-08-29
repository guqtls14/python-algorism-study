"""
 *packageName    : 
 * fileName       : 타겟 넘버
 * author         : ipeac
 * date           : 2022-08-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-29        ipeac       최초 생성
 """


def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    
    return answer


print(solution([1, 1, 1, 1, 1], 3))
# print(solution([4, 1, 2, 1], 4))
