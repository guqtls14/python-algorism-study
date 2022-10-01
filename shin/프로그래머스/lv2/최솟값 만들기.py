
# 시간초과
# def solution(A,B):
#     answer = 0
#     for _ in range(len(A)):
#         answer += min(A)*max(B)
#         A.remove(min(A))
#         B.remove(max(B))
#         if len(A) == 0 and len(B) == 0:
#             return answer
 
# 다른풀이

# def getMinSum(A,B):
#     return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))

# print(getMinSum([1,2],[3,4]))

from audioop import reverse


def solution(A,B):
    answer = 0
    A.sort(reverse = True)
    B.sort()
    for i in range(len(A)):
        answer += (A[i]*B[i])
    return answer
A=[1,2]
B=[3,4]
print(solution(A,B))

