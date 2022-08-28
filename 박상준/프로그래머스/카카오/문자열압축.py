"""
 *packageName    : 
 * fileName       : 문자열압축
 * author         : ipeac
 * date           : 2022-08-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-28        ipeac       최초 생성
 """


def solution(s):
    answer = 1001
    print(f"s : {s}")
    
    for i in range(1, len(s) // 2 + 1):
        tmp = s[:i]
        res = ''
        cnt = 1
        
        for j in range(i, len(s) + i, i):
            print("==========================================")
            print(f"tmp : {tmp}")
            if tmp == s[j:j + i]:
                cnt += 1
            else:  # 반복이 같지 않다면 tmp 새로운 문자로 초기화해야함
                if cnt == 1:
                    res += tmp
                    print(f"res : {res}")
                else:
                    res += str(cnt) + tmp
                    print(f"res : {res}")
                tmp = s[j:j + i]
                print(f"tmp : {tmp}")
                cnt = 1
        answer = answer if answer < len(res) else len(res)
    
    return answer


print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))
