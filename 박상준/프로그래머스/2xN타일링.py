"""
 *packageName    : 
 * fileName       : 2xN타일링
 * author         : ipeac
 * date           : 2022-09-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-02        ipeac       최초 생성
 """

#  가로 2 세로 1 직사각형 모양 타일
# 세로 2 가로 n 바닥을 채운다
# 채울 수 있는 경우의 수 리턴
import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 7)

@lru_cache(maxsize=None)
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def solution(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
        if i == n:
            return dp[n]

print(solution(9))
