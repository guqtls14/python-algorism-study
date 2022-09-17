"""
 *packageName    : 
 * fileName       : 2667.단지번호붙이기
 * author         : qkrtkdwns3410
 * date           : 2022-09-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-17        qkrtkdwns3410       최초 생성
 """
# 상 우 좌 하
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

# n = 7
# graph = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1],
#          [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def dfs(i, j):
    global cnt
    visited[i][j] = 1
    if graph[i][j] == 1:
        cnt += 1
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] == 1:
            dfs(nx, ny)

cnt = 0
total_cnt = 0
answer = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1:
            total_cnt += 1
            dfs(i, j)
            answer.append(cnt)
            cnt = 0
answer.sort()
print(total_cnt)
for i in answer:
    print(i)
