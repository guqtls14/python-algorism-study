"""
 *packageName    : 
 * fileName       : 정사각형의 개수 구하기
 * author         : ipeac
 * date           : 2022-08-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-21        ipeac       최초 생성
 """
import math


def solution(w, h):
    answer = 1
    
    gcd = math.gcd(w, h)
    answer = (w + h - gcd)
    answer = (w * h) - answer
    
    return answer


solution(8, 12)
