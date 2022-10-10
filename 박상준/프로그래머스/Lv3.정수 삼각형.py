"""
 *packageName    : 
 * fileName       : Lv3.정수 삼각형
 * author         : ipeac
 * date           : 2022-10-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-04        ipeac       최초 생성
 """

def solution(triangle):
    length = len(triangle)
    dp = [[-1] * j for j in range(1, length + 1)]  # dp 생성
    dp[0] = triangle[0]
    
    for i in range(length):
        if i == 0:
            continue
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    
    return max(dp[length - 1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
