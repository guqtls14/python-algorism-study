"""
 *packageName    : 
 * fileName       : 5212.지구 온난화
 * author         : ipeac
 * date           : 2022-10-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-02        ipeac       최초 생성
 """
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

# x축  = r   y축 == c
r, c = map(int, input().split())
graph = [list(map(str, input())) for _ in range(r)]
arr = []

# graph = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'X', 'X', 'X', '.', 'X', 'X', 'X', '.'], ['X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.']]

def zzap_bfs(x, y):
    inner_cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.':
            inner_cnt += 1
        elif 0 > nx or r <= nx or 0 > ny or c <= ny:  # 맵의 바깥은 전부 바다
            inner_cnt += 1
    
    return inner_cnt

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'X':
            cnt = zzap_bfs(i, j)
            if cnt >= 3:
                arr.append([i, j])

for value in arr:
    x, y = map(int, value)
    graph[x][y] = '.'

start_row = 0
end_row = 0
start_col = 0
end_col = 0
min_index = 1e9
max_index = -1e9

# 시작 행 계산
for i in range(r):
    if 'X' in graph[i]:
        start_row = i
        break

# 끝난 행 계산
for i in range(r - 1, -1, -1):
    if 'X' in graph[i]:
        end_row = i
        break

# 시작 열 계산
for i in range(start_row, end_row + 1):
    tmp = [i for i, value in enumerate(graph[i]) if value == 'X']  # x인 그래프의 열인덱스와 값을 담습니다.
    if not tmp:  # out of bound 방지
        continue
    min_tmp = tmp[0]
    max_tmp = tmp[-1]
    
    min_index = min(min_tmp, min_index)
    max_index = max(max_tmp, max_index)

start_col = min_index
end_col = max_index
for i in range(start_row, end_row + 1):
    for j in range(start_col, end_col + 1):
        print(graph[i][j], end="")
    print()
