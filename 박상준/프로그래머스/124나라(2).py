"""
 *packageName    : 
 * fileName       : 124나라(2)
 * author         : ipeac
 * date           : 2022-08-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-23        ipeac       최초 생성
 """
n_arr = ['4', '1', '2']


def solution(n):
    answer = ''
    while n > 0:
        if n % 3 == 0:
            answer += n_arr[n % 3]
            n //= 3
            n -= 1
        else:
            answer += n_arr[n % 3]
            n //= 3
    answer = answer[::-1]
    return answer


solution(9)
solution(6)
