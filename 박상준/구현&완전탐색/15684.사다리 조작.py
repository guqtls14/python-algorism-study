"""
 *packageName    : 
 * fileName       : 22251.빌런 호석
 * author         : ipeac
 * date           : 2022-09-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-19        ipeac       최초 생성
 """
# 세로선의 개수 n ; 가로선의 개수 m ; 세로선마다 가로선을 놓을 수 있는 위치의 개수 h
n, m, h = 5, 5, 6
h_arr = [[1, 1], [3, 2], [2, 3], [5, 1], [5, 4]]  # a : 번 점선 위치에서 연결 b : b번 세로선과 b+1 세로선을 연결함
board = [[0] * n for _ in range(h)]  # 특정 지점 방문 여부 체크
# n, m, h = map(int, input().split())
visited = [[False] * (n + 1) for _ in range(h + 1)]
combi = []
for i in range(m):
    a, b = map(int, h_arr[i])
    visited[a][b] = True


def check():
    for i in range(1, n + 1):
        now = i
        for j in range(1, h + 1):
            if visited[j][now - 1]:
                now -= 1
            elif visited[j][now]:
                now += 1
        if now != i:
            return False
    return True


def dfs(depth, idx):
    global answer
    if depth >= answer:
        return
    if check():
        answer = depth
        return

    for c in range(idx, len(combi)):
        x, y = combi[c]
        if not visited[x][y - 1] and not visited[x][y + 1]:
            visited[x][y] = True
            dfs(depth + 1, c + 1)
            visited[x][y] = False


for i in range(1, h + 1):
    for j in range(1, n):
        if not visited[i][j - 1] and not visited[i][j] and not visited[i][j + 1]:
            combi.append([i, j])  # 사다리 후보군 작성

answer = 4
dfs(0, 0)

print(answer if answer < 4 else -1)
