"""
 *packageName    : 
 * fileName       : k개수 제거시 가장 큰 숫자
 * author         : ipeac
 * date           : 2022-08-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-20        ipeac       최초 생성
 """


def solution(number, k):
    answer = ''
    number = list(map(int, number))
    
    print("number : %s " % number)
    stack = []
    for value in number:
        if not stack:
            stack.append(value)
            continue
        if k > 0:
            while stack[-1] < value:
                stack.pop()
                k -= 1
                if not stack or k <= 0:
                    break
        stack.append(value)
    print("stack : %s " % stack)
    for value in stack:
        answer += (str(value))
    
    return answer[:-k] if k > 0 else answer


solution("2222222", 4)
solution("1924", 2)
print("==========================================")
solution("1231234", 3)
print("==========================================")
solution("4177252841", 4)
print("==========================================")
