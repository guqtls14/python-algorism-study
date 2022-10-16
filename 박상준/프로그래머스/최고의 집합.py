"""
 *packageName    : 
 * fileName       : 최고의 집합
 * author         : ipeac
 * date           : 2022-10-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-16        ipeac       최초 생성
 """

def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    p, q = divmod(s, n)
    
    answer = [p] * n
    for i in range(q):
        answer[i] += 1
    
    return answer

# print(solution(2, 9))  # [4,5]
# print(solution(2, 1))
# print(solution(2, 8))
