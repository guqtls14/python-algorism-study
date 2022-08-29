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


def dfs(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        print(f"numbers : {numbers}")
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        answer += dfs(numbers, target, depth + 1)
        numbers[depth] *= -1
        answer += dfs(numbers, target, depth + 1)
        return answer


def solution(numbers, target):
    answer = dfs(numbers, target, 0)
    
    return answer


print(solution([1, 1, 1, 1, 1], 3))
# print(solution([4, 1, 2, 1], 4))
