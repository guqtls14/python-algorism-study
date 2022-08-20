"""
 *packageName    : 
 * fileName       : 가장 큰 수를 문자열로 변경
 * author         : ipeac
 * date           : 2022-08-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-18        ipeac       최초 생성
 """


def solution(numbers):
    print("numbers : %s " % numbers)
    answer = ''
    # 첫글자가 큰 순서대로 정렬
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    print("numbers : %s " % numbers)
    
    return answer


solution([6, 10, 2])
print("==========================================")
solution([3, 30, 34, 5, 9])
