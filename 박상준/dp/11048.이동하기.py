"""
 *packageName    : 
 * fileName       : 11048.이동하기
 * author         : ipeac
 * date           : 2022-09-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-23        ipeac       최초 생성
 """
# 준규가 (r, c)에 있으면, (r+1, c), (r, c+1), (r+1, c+1)로 이동할 수 있음
# 방향이동 제약
n, m = map(int, input().split())
# x 축 y축
miro = [list(map(int, input().split())) for _ in range(n)]
# miro = [[1, 2, 3, 4], [0, 0, 0, 5], [9, 8, 7, 6]]
answer = 0
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = miro[i - 1][j - 1] + max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
print(dp[n][m])
