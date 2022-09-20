"""
 *packageName    : 
 * fileName       : 1463.1로 만들기
 * author         : ipeac
 * date           : 2022-09-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-17        ipeac       최초 생성
 """
import sys

n = 10
cnt = 0

sys.setrecursionlimit(10 ** 9)

def dp(v):
    global cnt
    cnt += 1
    if v * 3 > n:
        if v * 2 > n:
            if v + 1 <= n:
                v += 1
                cnt += 1
            elif v + 1 > n:
                return cnt

        elif v * 2 <= n:
            v *= 2
            cnt += 1
    elif v * 3 <= n:
        v *= 3
        cnt += 1
    if v != n:
        dp(v)

print(dp(1))
