"""
 *packageName    : 
 * fileName       : 2606_바이러스
 * author         : qkrtkdwns3410
 * date           : 2022-09-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-06        qkrtkdwns3410       최초 생성
 """

c = int(input())
connect_cnt = int(input())
cc_arr = []
for i in range(connect_cnt):
    ss = input().split(" ")
    cc_arr.append([int(ss[0]), int(ss[1])])

answer = 0

def dfs(graph, idx, visited):
    global answer
    visited[idx] = 1
    for i in graph[idx]:
        if visited[i] == 0:
            dfs(graph, i, visited)
            answer += 1

def solution(c, cc_arr):
    global answer
    graph = [[] for _ in range(c + 1)]
    visited = [0] * (len(graph))
    
    for value in cc_arr:
        graph[value[0]].append(value[1])
        graph[value[1]].append(value[0])
    dfs(graph, 1, visited)
    print(answer)

solution(c, cc_arr)  # 4
