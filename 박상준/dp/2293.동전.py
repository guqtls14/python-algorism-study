"""
 *packageName    : 
 * fileName       : 2293.동전
 * author         : ipeac
 * date           : 2022-09-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-23        ipeac       최초 생성
 """

# n, k = map(int, input().split())
n, k = 3, 10
# coin_values = [int(input()) for _ in range(n)]
coin_values = [1, 2, 5]

dp = [0 for _ in range(k + 1)]

dp[0] = 1  # 인덱스 0의 경우 동전을 1개만 쓸 때의 경우의 수를 고려함.

for i in coin_values:  # 코인의 종류를 순회한다.
    for j in range(1, k + 1):  # 특정 가치를 가진 동전을 썼을 때 합이  j원이 되는 경우의 수 확인
        if j - i >= 0:
            dp[j] += dp[j - i]
            print(f"j : {j}")
            print(f"j-i : {j - i}")
            print("==========================================")
        print(f"dp : {dp}")
print(dp[k])
