"""
 *packageName    : 
 * fileName       : 최소 최대값 리턴
 * author         : ipeac
 * date           : 2022-08-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-18        ipeac       최초 생성
 """


def solution(s):
    answer = ''
    s = list(map(int, s.split(" ")))
    answer = answer + str(min(s)) + " "
    answer += str(max(s))
    return answer


solution("1 2 3 4")
print("==========================================")
solution("-1 -2 -3 -4")
print("==========================================")
solution("-1 -1")
