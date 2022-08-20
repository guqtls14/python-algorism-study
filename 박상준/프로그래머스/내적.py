"""
 *packageName    : 
 * fileName       : 내적
 * author         : ipeac
 * date           : 2022-08-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-18        ipeac       최초 생성
 """


def solution(a, b):
    answer = 0
    
    for index in range(len(a)):
        answer += a[index] * b[index]
    return answer


solution([1, 2, 3, 4], [-3, -1, 0, 2])
print("==========================================")
solution([-1, 0, 1], [1, 0, -1])
