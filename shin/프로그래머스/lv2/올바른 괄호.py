def solution(s):
    stack = []
    for i in s:
        if i == '(':  # '('는 stack에 추가
            stack.append(i)
        else:  # i == ')'인 경우
            if stack == []:  # 괄호 짝이 ')'로 시작하면 False 반환
                return False
            else:
                stack.pop()  # '('가 ')'와 짝을 이루면 stack에서 '(' 하나 제거
    
    return stack==[]


# def is_pair(s):
#     # 함수를 완성하세요
#     open_cnt = 0
#     for c in s:
#         if c == '(':
#             open_cnt += 1
#         elif c == ')':
#             open_cnt -= 1
#             if open_cnt < 0:
#                 return False
#     return open_cnt == 0


# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print( is_pair("(hello)()"))
# print( is_pair(")("))