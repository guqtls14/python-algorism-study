"""
 *packageName    : 
 * fileName       : 빛의 경로 사이클
 * author         : qkrtkdwns3410
 * date           : 2022-09-15
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-15        qkrtkdwns3410       최초 생성
 """
# 우상 좌하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def solution(grid):
    answer = []
    
    row, col = len(grid), len(grid[0]),
    visited = [[[0] * 4 for _ in range(col)] for _ in range(row)]
    
    def move(x, y, dir, pos):
        # dir 우 상 좌 하
        # 우 -> 상 좌 -> 하 상 -> 좌 하->우
        if pos == 'L':
            dir = (dir + 1) % 4
        elif pos == 'R':
            dir = (dir - 1) % 4
        x = (x + dx[dir]) % row
        y = (y + dy[dir]) % col
        
        return x, y, dir
    
    for i in range(row):
        for j in range(col):
            for k in range(4):
                if visited[i][j][k] == 0:
                    cnt = 0
                    x, y, dir = i, j, k
                    
                    while not visited[x][y][dir]:
                        cnt += 1
                        visited[x][y][dir] = 1
                        x, y, dir = move(x, y, dir, grid[x][y])
                    answer.append(cnt)
    
    return answer

print(solution(["SL", "LR"]))
# print(solution(["S"]))
# print(solution(["R", "R"]))
