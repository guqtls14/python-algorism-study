"""
 *packageName    : 
 * fileName       : 1463.1로 만들기
 * author         : qkrtkdwns3410
 * date           : 2022-09-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-18        qkrtkdwns3410       최초 생성
 """

n = 10

dp = [0] * 100001

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1  # dp[3] = dp[2] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])
