"""
 *packageName    : 
 * fileName       : 1463.1로 만들기(2)
 * author         : ipeac
 * date           : 2022-09-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-23        ipeac       최초 생성
 """
n = int(input())

dp = [0] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1  # 2와 3으로 나뉘지 않는 경우 => 1로 빼준다.
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)  # 나눈 횟수를 저장위해 1을 더한다.
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
print(dp[n])
