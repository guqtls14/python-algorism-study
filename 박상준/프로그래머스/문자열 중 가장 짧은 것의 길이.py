"""
 *packageName    : 
 * fileName       : 문자열 중 가장 짧은 것의 길이
 * author         : ipeac
 * date           : 2022-08-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-18        ipeac       최초 생성
 """


def solution(s):
    answer = 0
    print("s : %s " % s)
    
    for i in range(1, len(s) // 2 + 1):
        b = ''
        cnt = 1
        temp = s[:i]
        for j in range(i, len(s) + 1, i):  # i 부터 끝까지 i 단위로 나누어 탐색
            ss = s[j:j + i]
            
            if temp == s[j:j + i]:  # 앞과 동일하면 cnt
                cnt += 1
            else:
                if cnt != 1:  # 앞에서 중복이 있음.
                    b = b + str(cnt) + temp
                else:
                    b = b + temp
                temp = s[j:j + i]
                cnt = 1
    return answer


solution("aabbaccc")
print("==========================================")
solution("ababcdcdababcdcd")
print("==========================================")
solution("abcabcdede")
print("==========================================")
solution("abcabcabcabcdededededede")
print("==========================================")
solution("xababcdcdababcdcd")
print("==========================================")
