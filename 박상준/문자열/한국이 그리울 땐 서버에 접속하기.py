"""
 *packageName    : 
 * fileName       : 한국이 그리울 땐 서버에 접속하기
 * author         : qkrtkdwns3410
 * date           : 2022-09-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-06        qkrtkdwns3410       최초 생성
 """

# 파일의 개수
tc = int(input())
p = input()
strs = []
for i in range(tc):
    strs.append(input())

def solution(tc, p, strs):
    p_s, p_e = p.split("*")
    for string in strs:
        if len(p_s) + len(p_e) > len(string):
            print("NE")
            continue
        if string.startswith(p_s) and string.endswith(p_e):
            print("DA")
        else:
            print("NE")

solution(tc, p, strs)
