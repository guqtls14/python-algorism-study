# def solution(s):
#     answer = True
    
#     tmp=[]

#     for i in s:
#         if i == '(':
#             tmp.append(i)
#         else:
#             if len(tmp)>0:
#                 tmp.pop()
#             else:
#                 answer=False
#     if tmp == []:
#         answer= True
#     else:
#         answer = False
#     return answer
# word="(())()"
# print(solution(word))

def solution(s):

    
    tmp=[]

    for i in s:
        if i == '(':
            tmp.append(i)
        else:
            if len(tmp)>0:
                tmp.pop()
            else:
                return False
    if tmp == []:
        return True

  
word="()())"
print(solution(word))