# 완전탐색
def solution(s):
    answer=0
    for i in range(1,s+1):
        sum=0
        for j in range(i,s+1):
            sum+=j
            if sum == s:
                answer+=1
                break
            elif sum > s:
                break
    return answer
word=15
print(solution(word))

# def expressions(num):
#     answer = 0
#     for i in range(1, num + 1):
#         s = 0
#         while s < num:
#             s += i
#             i += 1
#         if s == num:
#             answer += 1


#     return answer