"""
 *packageName    : 
 * fileName       : 짝지어 제거하기
 * author         : ipeac
 * date           : 2022-09-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-01        ipeac       최초 생성
 """

def solution(s):
    if len(s) % 2 == 1:
        return 0
    if len(s) == 2:
        return 1 if s[0] == s[1] else 0
    
    stack = [s[0]]
    
    for v in s[1:]:
        if len(stack) > 0 and stack[-1] == v:
            stack.pop()
        else:
            stack.append(v)
    
    if len(stack) == 0:
        return 1
    else:
        return 0

print(solution("baabaa"))
print(solution("cdcd"))
