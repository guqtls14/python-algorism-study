"""
 *packageName    : 
 * fileName       : 2294.동전2
 * author         : ipeac
 * date           : 2022-09-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-23        ipeac       최초 생성
 """
n, k = map(int, input().split())
coin_value = [int(input()) for _ in range(n)]

dp = [10001 for _ in range(k + 1)]
dp[0] = 0
coin_value.sort()

for i in coin_value:
    for j in range(i, k + 1):
        dp[j] = min(dp[j], dp[j - i] + 1)

if dp[k] == 10001:
    print(-1)
    exit(0)

print(dp[k])
