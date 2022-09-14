"""
 *packageName    : 
 * fileName       : n^2 배열 자르기
 * author         : ipeac
 * date           : 2022-09-14
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-14        ipeac       최초 생성
 """


def solution(n, left, right):
    answer = []
    """몫과 나머지를 활용하여 출력할 부분만 출력함"""
    for i in range(left, right + 1):
        # 몫
        mock = i // n
        # 나머지
        na = i % n
        if na <= mock:
            answer.append(mock + 1)
        else:
            answer.append(na + 1)
    
    return answer


# solution(3, 2, 5)
solution(4, 7, 14)
