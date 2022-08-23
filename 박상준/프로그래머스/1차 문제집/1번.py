"""
 *packageName    : 
 * fileName       : 1번
 * author         : ipeac
 * date           : 2022-08-22
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-22        ipeac       최초 생성
 """
from collections import Counter


def solution(X, Y):
    x, y = Counter(X), Counter(Y)
    answer = []
    for num in range(9, -1, -1):
        num = str(num)
        if num in x and num in y:
            for i in range(min(x[num], y[num])):
                answer.append(num)
    
    if not answer:
        return "-1"
    if answer[0] == '0':
        return '0'
    
    return "".join(answer)


# solution("111", "111111111111111111")
# print("==========================================")
solution("100", "12345")
print("==========================================")
# solution("100", "203045")
# print("==========================================")
# solution("100", "123450")
# print("==========================================")
# solution("12321", "42531")
# print("==========================================")
# solution("5525", "1255")
# print("==========================================")
# solution("3403", "13203")  # 330
# print("==========================================")
