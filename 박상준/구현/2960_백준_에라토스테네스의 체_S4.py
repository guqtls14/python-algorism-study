"""
 *packageName    : 
 * fileName       : 2960_백준_에라토스테네스의 체_S4
 * author         : ipeac
 * date           : 2022-07-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-26        ipeac       최초 생성
 """
"""
7 3
6

15 12
7

10 7
9
"""
n, k = map(int, input().split())
graph = [value for value in range(2, n + 1)]
k_count = 1
while True:
    p = min(graph)
    for value in range(2, p):
        if p % value == 0:
            break

    for value in range(p, n + 1, p):
        try:
            index = graph.index(value)

            if k_count == k:
                print(graph[index])
                exit(0)

            graph.pop(index)
            k_count += 1
            if len(graph) == 0:
                exit()

        except ValueError:
            pass
