"""
 *packageName    : 
 * fileName       : JadenCase문자열 만들기
 * author         : ipeac
 * date           : 2022-09-14
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-14        ipeac       최초 생성
 """


def solution(s):
    answer = ''
    s_list = list(map(str, s))
    flag = True
    for i, value in enumerate(s_list):
        if value == " ":
            flag = True
            answer += value
            continue
        if flag and value.isalpha():  # 플래그가 true라면
            answer += s_list[i].upper()  # 대문자 변경
            flag = False
        elif not flag and value.isalpha():  # 나머지 문자가 대문자라면
            answer += s_list[i].lower()  # 소문자 변경
        elif flag and value.isnumeric():
            answer += s_list[i]
            flag = False
        elif not flag and value.isnumeric():
            answer += s_list[i]
    
    return answer


# solution(" t t t  ")
# solution("for  the last week")
# solution("3people unFollowed me")
solution(" Aaaaa Aaa")
