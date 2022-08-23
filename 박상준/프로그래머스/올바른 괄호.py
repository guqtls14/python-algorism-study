"""
 *packageName    : 
 * fileName       : 올바른 괄호
 * author         : ipeac
 * date           : 2022-08-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-23        ipeac       최초 생성
 """


def solution(s):
    cnt = 0
    for value in s:
        if value == '(':
            cnt += 1
        elif value == ')':
            cnt -= 1
            if cnt < 0:
                return False
    return True if cnt == 0 else False


solution("(())()")
