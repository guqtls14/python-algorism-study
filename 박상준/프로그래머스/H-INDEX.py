"""
 *packageName    : 
 * fileName       : H-INDEX
 * author         : ipeac
 * date           : 2022-09-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-03        ipeac       최초 생성
 """

def solution(citations):
    answer = 0
    length = len(citations)
    # h 번 인용된 논문이 h편 이상이고
    # 나머지가 h 번 이하 인용 h의 최댓값이 H-INDEX
    citations.sort()
    for h in range(max(citations)):
        count = 0
        for n in range(len(citations)):
            if h <= citations[n]:
                count += 1
        if count >= h:
            answer = max(answer, h)
    return answer

print(solution([3, 0, 6, 1, 5]))
