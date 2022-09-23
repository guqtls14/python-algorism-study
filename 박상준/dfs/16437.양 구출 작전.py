"""
 *packageName    : 
 * fileName       : 16437.양 구출 작전
 * author         : ipeac
 * date           : 2022-09-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-20        ipeac       최초 생성
 """
import sys

sys.setrecursionlimit(10 ** 6)

n = 4

# tree = [[] for _ in range(n + 1)]
# node = [[], [0, 0]]

# 1. 트리 구조 만들기
# for i in range(n - 1):
#     kind, number, connection = input().split()
#     tree[int(connection)].append(i + 1)
#     node.append([kind, int(number)])
# print(f"tree : {tree}")
# print(f"node : {node}")

tree = [[], [2, 3], [], [1], []]
node = [[], [0, 0], ['S', 100], ['W', 50], ['S', 10]]

# 2 .dfs를 이용하여 탐색하기
def dfs(v):  # v : 현재 노드
    result = 0
    
    # 노드들을 탐색하며 더해준다.
    for i in tree[v]:
        result += dfs(i)
    
    # 노드의 타입이 늑대라면 빼준다.
    if node[v][0] == 'W':
        result -= node[v][1]
        if result < 0:
            result = 0
    # 노드의 타입이 양이라면 더한다.
    else:
        result += node[v][1]
    return result

print(dfs(1))
