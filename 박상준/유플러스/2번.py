"""
 *packageName    : 
 * fileName       : 2번
 * author         : ipeac
 * date           : 2022-10-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-01        ipeac       최초 생성
 """
from collections import deque

def solution(compressed):
    if not compressed:
        return ""
    start, end = [], 0
    while end < len(compressed):
        if compressed[end].isdigit():
            num = 0
            while end < len(compressed) and compressed[end].isdigit():
                num = num * 10 + int(compressed[end])
                end += 1
            start.append(num)
        elif compressed[end] == "(":
            start.append("(")
            end += 1
        elif compressed[end].isalpha():
            tmp = []
            while end < len(compressed) and compressed[end].isalpha():
                tmp.append(compressed[end])
                end += 1
            start.append("".join(tmp))
        elif compressed[end] == ")":
            q = deque()
            while start[-1] != "(":
                q.appendleft(start[-1])
                start.pop()
            start.pop()
            if start and type(start[-1]) is int:
                temp_str = "".join(q) * start[-1]
                start.pop()
                start.append(temp_str)
            end += 1
    return "".join(start)

# print(solution("3(hi)"))
print(solution("2(3(hi)co)"))
# print(solution("10(p)"))
# print(solution("2(2(hi)2(co))x2(bo)"))
