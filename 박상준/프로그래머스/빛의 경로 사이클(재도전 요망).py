"""
 *packageName    : 
 * fileName       : 빛의 경로 사이클
 * author         : ipeac
 * date           : 2022-08-30
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-30        ipeac       최초 생성
 """

# 상 우 하 좌
import pprint

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solution(grid):
    answer = []
    global row, col
    row, col = len(grid), len(grid[0])
    visited = [[[False] * 4 for _ in range(col)] for _ in range(row)]
    pprint.pprint(visited)
    
    def move(x, y, dir, pos):
        # dir 0 상 1 우 2 좌 3 하
        print(f"x,y,dir,pos : {x, y, dir, pos}")
        
        if pos == 'L':  # 좌로 가는데 L을 만나면 하, 우로 가는데 L을 만나면 상
            dir = (dir - 1) % 4
        elif pos == 'R':
            dir = (dir + 1) % 4
        
        nx = (x + dx[dir]) % row
        ny = (y + dy[dir]) % col
        print(f"nx,ny,dir : {nx, ny, dir}")
        
        return nx, ny, dir
    
    for i in range(row):
        for j in range(col):
            for k in range(4):  # 네 방향에 대하여 확인
                if not visited[i][j][k]:
                    route = 0
                    x, y, dir = i, j, k
                    print(f"x,y,dir : {x, y, dir}")
                    
                    while not visited[x][y][dir]:
                        route += 1
                        visited[x][y][dir] = True
                        x, y, dir = move(x, y, dir, grid[x][y])
                    
                    answer.append(route)
    
    answer.sort()
    return answer

print(solution(["SL", "LR"]))
