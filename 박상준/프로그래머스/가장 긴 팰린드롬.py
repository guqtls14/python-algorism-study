"""
 *packageName    : 
 * fileName       : 가장 긴 팰린드롬
 * author         : ipeac
 * date           : 2022-10-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-17        ipeac       최초 생성
 """

def isPal(s):
    if s == s[::-1]:
        return True
    return False

def solution(s):
    max_length = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            tmp = s[i:j]
            if isPal(tmp):
                max_length = max(max_length, len(tmp))
    
    return max_length

print(solution("abcdcba"))
# print(solution("abacde"))
