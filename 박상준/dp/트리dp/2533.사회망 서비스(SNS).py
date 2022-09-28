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
n = int(input())
tree = [[] for _ in range(n + 1)]

# 트리 생성
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# Node 가 1번부터  N개 주어진다.
visited = [False] * (n + 1)

# [ 내가 ea 아닐 때 ea 수 , 내가 ea일 때 ea 수]
# ea = 얼리어답터
dp_mat = [[0, 1] for _ in range(n + 1)]

def dp(cur):
    # 어디를 시작점으로 잡아도 상관없음..
    # 이미 방문한 곳을 다시 방문하는 건 안됨
    # 현재 node cur
    visited[cur] = True
    
    for nei in tree[cur]:
        # 아직 방문 X -> nei는 cur의 child! 재귀 수행
        if not visited[nei]:
            dp(nei)  # Leaf node까지 내려간다.
            
            # Node cur이 ea가 아니면, child가 무조건 ea여야한다.
            dp_mat[cur][0] += dp_mat[nei][1]
            
            # Node cur 이 ea라면 , child가 ea든 아니든 상관없음
            dp_mat[cur][1] += min(dp_mat[nei][0], dp_mat[nei][1])

# 어느곳을 시작점으로 잡든 상관없다
dp(n - 1)

# 시작점이 ea인 경우, 아닌경우 2가지 모두 돌려보고,
# 작은 case를 출력한다.
print(min(dp_mat[n - 1][0], dp_mat[n - 1][1]))
