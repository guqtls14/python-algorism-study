"""
 *packageName    : 
 * fileName       : 15681.트리와 쿼리
 * author         : ipeac
 * date           : 2022-09-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-28        ipeac       최초 생성
 """
# 정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력한다.
# 트리의 정점 N || 루트의 번호 R, 쿼리의 수 Q
# n, r, q = map(int, input().split())
n, r, q = 9, 5, 3
node = [[] for _ in range(n + 1)]
u = []
# 양방향 간선 설정
# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     node[a].append(b)
#     node[b].append(a)
node = [[], [3], [3], [1, 4, 2], [3, 5], [4, 6], [5, 7, 9, 8], [6], [6], [6]]
# 쿼리 수
# for _ in range(q - 1):
#     k = int(input())
#     u.append(k)
u = [5, 4, 8]
visited = [0] * (n + 1)

def dp(cur):
    visited[cur] = 1
    
    for ne in node[cur]:
        print("==========================================")
        if not visited[ne]:
            print(f"ne : {ne}")
            dp(ne)  # 결국에는 최하단까지 내려가게될거임
            print(f"visited[ne] : {visited[ne]}")
            visited[cur] += visited[ne]  # 밑에서부터 현재 노드에 아래의 값들을 더해주게되는거 visited 된 값들은 1일테니까

dp(r)
for i in u:
    print(visited[i])
