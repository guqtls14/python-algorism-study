"""
 *packageName    : 
 * fileName       : 2533.사회망 서비스(SNS)
 * author         : ipeac
 * date           : 2022-09-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-27        ipeac       최초 생성
 """
n = 8
lines = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)
dp = [[0, 0] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

def dfs(r):
    visited[r] = 1  # 방문여부 확인
    dp[r][0] = 1
    # dp[?][0] = 노드가 얼리어답터인 경우 서브 트리에서의 얼리어답터의 최소값
    # dp[?][1] = 노드가 얼리어답터가 아닌경우 서브 트리에서의 얼리어답터의 최소값
