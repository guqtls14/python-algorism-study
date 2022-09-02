"""
 *packageName    : 
 * fileName       : 괄호 회전하기
 * author         : qkrtkdwns3410
 * date           : 2022-09-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-02        qkrtkdwns3410       최초 생성
 """

# s 를 왼쪽으로 회전 > x (0<= x < (s의 길이 만큼))
def solution(s):
    answer = 0
    temp = list(s)
    # 리스트의 길이만큼 for문 반복 리스트 회전
    for _ in range(len(s)):
        stack = []
        # 스택에 아무것도 없다면 괄호를 추가 || 같으면 제거
        for j in range(len(temp)):
            if len(stack) > 0:
                if stack[-1] == '(' and temp[j] == ')':
                    stack.pop()
                elif stack[-1] == '[' and temp[j] == ']':
                    stack.pop()
                elif stack[-1] == '{' and temp[j] == '}':
                    stack.pop()
                # 스택 길이가 0이라면 추가해야함
                else:
                    stack.append(temp[j])
            else:
                stack.append(temp[j])
        if len(stack) == 0:
            answer += 1
        temp.append(temp.pop(0))
    
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
