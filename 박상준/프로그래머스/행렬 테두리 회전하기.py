"""
 *packageName    : 
 * fileName       : 행렬 테두리 회전하기
 * author         : ipeac
 * date           : 2022-08-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-29        ipeac       최초 생성
 """

def solution(rows, columns, queries):
    answer = []
    graph = [list([0] * columns) for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = num
            num += 1
    
    for query in queries:
        tmp = [item[:] for item in graph]
        x1, y1, x2, y2 = map(int, query)
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        
        temp_num = tmp[x2][y1 + 1]
        min_num = temp_num
        # 왼쪽 세로 옮기기
        for x in range(x2, x1 - 1, -1):
            graph[x][y1] = temp_num
            temp_num = tmp[x][y1]
            min_num = min(min_num, temp_num)
        # 위 옮기기
        for y in range(y1 + 1, y2 + 1):
            graph[x1][y] = temp_num
            temp_num = tmp[x1][y]
            min_num = min(min_num, temp_num)
        
        # 오른쪽 세로 옮기기
        for x in range(x1 + 1, x2 + 1):
            graph[x][y2] = temp_num
            temp_num = tmp[x][y2]
            min_num = min(min_num, temp_num)
        
        # 아래 옮기기
        for y in range(y2 - 1, y1 - 1, -1):
            graph[x2][y] = temp_num
            temp_num = tmp[x2][y]
            min_num = min(min_num, temp_num)
        answer.append(min_num)
    return answer

# print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 3, 3]]))
# print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
# print(solution(100, 97, [[1, 1, 100, 97]]))
