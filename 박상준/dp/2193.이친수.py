"""
 *packageName    : 
 * fileName       : 2193.이친수
 * author         : ipeac
 * date           : 2022-09-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-23        ipeac       최초 생성
 """

n = int(input())

dp = [0 for _ in range(n + 1)]
dp[1] = 1
if n == 1:
    print(dp[1])
    exit()
dp[2] = 1

if n == 2:
    print(dp[2])
    exit()
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])
