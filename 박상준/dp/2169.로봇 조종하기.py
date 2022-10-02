"""
 *packageName    : 
 * fileName       : 2169.로봇 조종하기
 * author         : ipeac
 * date           : 2022-09-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-26        ipeac       최초 생성
 """
import pprint

dx = [0, 0, 1]
dy = [1, -1, 0]

# n x 좌표 m : y 좌표
n, m = 5, 5
# grid = [list(map(int, input().split())) for _ in range(m)]
grid = [[10, 25, 7, 8, 13], [68, 24, -78, 63, 32], [12, -69, 100, -29, -25], [-16, -22, -57, -33, 99], [7, -76, -11, 77, 15]]

# 맨 윗줄 오른쪽만 가능함
for i in range(1, m):
    grid[0][i] += grid[0][i - 1]
    print(f"grid : {grid}")
# 다음줄 부터는 왼 오
for j in range(1, n):  # 나머지 x좌표 계산 위 배열과 합산 + 왼쪽합산 오른쪽 합산의 최대값을 getter
    startLeft = [grid[i][j] + grid[i - 1][j] for j in range(m)]
    startRight = [grid[i][j] + grid[i - 1][j] for j in range(m)]
    
    pass
