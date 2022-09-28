# 전위:부,왼,오
# 중위:왼,부,오
# 후회:왼,오,부

# 왼쪽노드: 부모노드*2
# 오른쪽노드: 부모노드*2+1

def DFS(x):
    if x>7:
        return
    else:
        # 자기걸먼저하고 함수호출하면 전위순열(대부분전위임..)
        print(x,end=' ')
        DFS(x*2)
        DFS(x*2+1)

# def DFS(x):
#     if x>7:
#         return
#     else:
#         DFS(x*2)
#         # 중위
#         print(x,end=' ')
#         DFS(x*2+1)

# def DFS(x):
#     if x>7:
#         return
#     else:
#         DFS(x*2)
#         print(x,end=' ')
#         # 후위, 대표적으로 병합정렬
#         DFS(x*2+1)
DFS(1)