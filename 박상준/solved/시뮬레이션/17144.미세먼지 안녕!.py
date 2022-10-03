"""
 *packageName    : 
 * fileName       : 17144.미세먼지 안녕!
 * author         : ipeac
 * date           : 2022-10-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-03        ipeac       최초 생성
 """

dx = [0, -1, 0, 1]  # 우 상 좌 하
dy = [1, 0, -1, 0]

R, C, T = 7, 8, 1
# A = [list(map(int, input().split())) for _ in range(R)]
A = [[0, 0, 0, 0, 0, 0, 0, 9], [0, 0, 0, 0, 3, 0, 0, 8], [-1, 0, 5, 0, 0, 0, 22, 0], [-1, 8, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 10, 43, 0], [0, 0, 5, 0, 15, 0, 0, 0], [0, 0, 40, 0, 0, 0, 20, 0]]

# 공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다.
# -1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.
# , T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양을 구해보자.

# 공기 청정기 위치 찾기
for i in range(R):
    if A[i][0] == -1:
        up = i
        down = i + 1
        break

def spread():
    tmp_arr = [[0] * C for _ in range(R)]  # 임시 배열 생성
    for i in range(R):
        for j in range(C):
            if A[i][j] != 0 and A[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and A[nx][ny] != -1:
                        tmp_arr[nx][ny] += A[i][j] // 5
                        tmp += A[i][j] // 5
                A[i][j] -= tmp
    for i in range(R):
        for j in range(C):
            A[i][j] += tmp_arr[i][j]

def air_up():
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break  # 공기청정기에 도달한다면
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        A[x][y], before = before, A[x][y]  # 해당 칸의 전값이 들어가게되며 before 는 깨끗한 공기가 분출된다.
        x = nx  # 이동한 값을 X y 에 저장
        y = ny

def air_down():
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct -= 1
            continue
        A[x][y], before = before, A[x][y]
        x = nx
        y = ny

for _ in range(T):
    spread()
    air_up()
    air_down()

answer = 0
for i in range(R):
    for j in range(C):
        if A[i][j] > 0:
            answer += A[i][j]
print(answer)
