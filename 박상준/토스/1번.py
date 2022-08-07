"""
 *packageName    : 
 * fileName       : 1번
 * author         : jihye94
 * date           : 2022-08-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-06        jihye94       최초 생성
 """


def solution(s):
    s_arr = list(map(str, s))
    max_num = 0
    max_count = 0
    count = 0
    
    for i in range(len(s_arr) - 1):
        if s_arr[i] == s_arr[i + 1]:
            count += 1
        else:
            if max_count <= count and max_num < int(s_arr[i]) and count >= 1:
                max_count = count
                max_num = int(s_arr[i])
                count = 0
    
    if max_count == 0 and count == 0:
        return -1
    
    answer = ""
    
    if max_count == 0:
        max_count = count
    
    for i in range(max_count + 1):
        answer += str(max_num)
    print("answer : %s " % answer)
    return int(answer.rstrip())


solution("000")
print("==========================================")
solution("12223")
print("==========================================")
solution("111999333")
print("==========================================")
solution("123")
