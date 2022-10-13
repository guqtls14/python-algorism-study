"""
 *packageName    : 
 * fileName       : H-index
 * author         : ipeac
 * date           : 2022-10-13
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-13        ipeac       최초 생성
 """

def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    for h in range(citations[-1]):
        cnt = 0
        for j in range(0, len(citations)):
            quotation = citations[j]  # 인용수
            if h <= quotation:
                cnt += 1
        if cnt >= h >= (n - cnt):
            answer = h
    
    return answer

print(solution([3, 0, 6, 1, 5]))
