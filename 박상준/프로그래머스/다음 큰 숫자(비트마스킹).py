"""
 *packageName    : 
 * fileName       : 다음 큰 숫자(비트마스킹)
 * author         : ipeac
 * date           : 2022-08-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-23        ipeac       최초 생성
 """


def next_big_number(n):
    c = bin(n).count('1')
    for m in range(n + 1, 1000001):
        if bin(m).count('1') == c:
            return m


def solution(n):
    number = next_big_number(n)
    return number


solution(78)
