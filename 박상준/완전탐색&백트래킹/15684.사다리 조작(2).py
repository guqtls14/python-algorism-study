"""
 *packageName    : 
 * fileName       : 15684.사다리 조작(2)
 * author         : ipeac
 * date           : 2022-09-30
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-30        ipeac       최초 생성
 """
# h
n, m, h = map(int, input().split())
visited = [[False] * (n + 1) for _ in range(h + 1)]
data = []
for _ in range(m):
    a, b = map(int, input().split())
    visited[a][b] = True

def check():  # i 로 시작하여  i로 떨어지는지 체크합니다.
    for i in range(1, n + 1):  # 세로선 개수
        now = i
        for j in range(1, h + 1):  # 놓을 수 있는 세로선
            if visited[j][now - 1]:
                now -= 1
            elif visited[j][now]:
                now += 1
        if now != i:
            return False
    return True

def dfs(depth, index):
    global result
    if depth >= result:
        return
    if check():
        result = depth
        return
    
    for c in range(index, len(data)):
        x, y = data[c]
        if not visited[x][y - 1] and not visited[x][y + 1]:
            visited[x][y] = True
            dfs(depth + 1, c + 1)
            visited[x][y] = False

for i in range(1, h + 1):  # h 의 놓을 수 있는 가로선
    for j in range(1, n):  # n개의 세로선
        if not visited[i][j - 1] and not visited[i][j] and not visited[i][j + 1]:
            data.append([i, j])

result = 4
dfs(0, 0)

if result < 4:
    print(result)
else:
    print(-1)
