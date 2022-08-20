"""
 *packageName    : 
 * fileName       : 연구소점프
 * author         : ipeac
 * date           : 2022-08-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-18        ipeac       최초 생성
 """
import math


def solution(n):
    print("n : %s " % n)
    ans = 0
    walk = 1
    cnt = 1
    while n > 0:
        cnt += n % 2
        print("cnt : %s " % cnt)
        n //= 2
        print("n : %s " % n)
        pass
    return ans


solution(5)
print("==========================================")
solution(6)
print("==========================================")
solution(5000)
print("==========================================")
