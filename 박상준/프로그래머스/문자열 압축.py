"""
 *packageName    : 
 * fileName       : 문자열 압축
 * author         : ipeac
 * date           : 2022-08-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-21        ipeac       최초 생성
 """


def solution(s):
    answer = 10000
    for n in range(1, len(s) // 2 + 1):
        res = ''
        cnt = 1
        tmp = s[:n]  # 단위문자열 초기화
        
        for i in range(n, len(s) + n, n):
            if tmp == s[i:i + n]:
                cnt += 1
            else:
                if cnt == 1:
                    res += tmp
                else:
                    res += str(cnt) + tmp
                tmp = s[i:i + n]
                cnt = 1
        # print(res)
        answer = min(answer, len(res))
    return answer


solution("aabbaccc")
print("==========================================")
# solution("ababcdcdababcdcd")
# print("==========================================")
# solution("abcabcdede")
# print("==========================================")
# solution("abcabcabcabcdededededede")
# print("==========================================")
# solution("xababcdcdababcdcd")
# print("==========================================")
