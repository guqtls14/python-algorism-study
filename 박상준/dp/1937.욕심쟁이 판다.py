"""
 *packageName    : 
 * fileName       : 1937.욕심쟁이 판다
 * author         : ipeac
 * date           : 2022-09-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-26        ipeac       최초 생성
 """
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 대나무 숲의 크기 n
n = int(input())
# 대나무 숲의 정보
woods = [list(map(int, input().split())) for _ in range(n)]
# woods = [[14, 9, 12, 10], [1, 11, 5, 4], [7, 15, 2, 13], [6, 3, 16, 8]]
dp = [[-1] * n for _ in range(n)]

def dfs(i, j):
    if dp[i][j] == -1:  # 다녀감 처리
        dp[i][j] = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            # dfs 가 배열을 벗어나지 않도록 체크 && 이전 우드 배열의 값보다 커야 판다가 먹음
            if 0 <= nx < n and 0 <= ny < n and woods[i][j] < woods[nx][ny]:
                print(f"dp[nx][ny] : {dp[nx][ny]}")
                print(f"dp[i][j] : {dp[i][j]}")
                print(dfs(nx, ny))
                dp[nx][ny] = max(dp[i][j], dfs(nx, ny))  # 원 dp값 과 nx,ny값의 dfs 처리한 값의 +1 값의 비교
        dp[i][j] += 1
    return dp[i][j]

ans = 0
# 2차원 배열 dp # 모든 공간 탐색 # 최대한 많은 칸을 이동
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))
print(ans)
