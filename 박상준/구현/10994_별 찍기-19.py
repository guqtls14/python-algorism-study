"""
 *packageName    : 
 * fileName       : 10994_별 찍기-19
 * author         : ipeac
 * date           : 2022-09-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-06        ipeac       최초 생성
 """

n = int(input())

def draw(n, idx, star_graph):
    length = 4 * n - 3
    if n == 1:
        star_graph[idx][idx] = '*'
        return star_graph
    
    for i in range(idx, idx + length):
        star_graph[idx][i] = '*'
        star_graph[idx + length - 1][i] = '*'
        star_graph[i][idx] = '*'
        star_graph[i][idx + length - 1] = '*'
    return draw(n - 1, idx + 2, star_graph)

def solution(n):
    length = 4 * n - 3
    
    star_graph = [[' '] * length for _ in range(length)]
    
    star_graph = draw(n, 0, star_graph)
    for i in star_graph:
        for j in i:
            print(j, end="")
        print()

solution(n)
