"""
 *packageName    : 
 * fileName       : 나누기
 * author         : ipeac
 * date           : 2022-08-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-18        ipeac       최초 생성
 """


def solution(arr, divisor):
    print("arr : %s " % arr)
    print("divisor : %s " % divisor)
    answer = []
    # divisor로 나누어 떨어지는 값을 오름차순 정렬한 배열 반환.
    for value in arr:
        if value % divisor == 0:
            answer.append(value)
    # divisor로 나누어 떨어지는 요소가 없다면 배열에 -1
    
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer


solution([5, 9, 7, 10], 5)
print("==========================================")
solution([2, 36, 1, 3], 1)
print("==========================================")
solution([3, 2, 6], 10)
