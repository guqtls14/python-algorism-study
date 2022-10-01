def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        # capitalize 내장함수를 사용하면 첫 문자가 알파벳일 경우 대문자로 만들고
        # 두번째 문자부터는 자동으로 소문자로 만든다
        # 첫 문자가 알파벳이 아니면 그대로 리턴한다
        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer

word="3people unFollowed me"

print(solution(word))


# def solution(s):
#     answer=''
#     s=s.split(' ')
#     for i in range(len(s)):
#         if not s[i][0].isdecimal():
#             s[i]=s[i][0].upper()+s[i][1:].lower()
#     answer=' '.join(s)
#     return answer

# def Jaden_Case(s):
#     # 함수를 완성하세요
#     answer =[]
#     for i in range(len(s.split())):
#         answer.append(s.split()[i][0].upper() + s.split()[i].lower()[1:]) 
#     return " ".join(answer)