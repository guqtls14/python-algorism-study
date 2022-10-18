"""
 *packageName    : 
 * fileName       : 54. Spiral Matrix
 * author         : ipeac
 * date           : 2022-10-13
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-13        ipeac       최초 생성
 """
from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    answer = []
    if len(matrix) == 0:
        return answer
    
    m, n = len(matrix[0]), len(matrix)  # 세로 가로
    left, right, top, bottom = 0, m - 1, 0, n - 1
    
    while left <= right and top <= bottom:
        for col in range(left, right + 1):
            answer.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):
            answer.append(matrix[row][right])
        right -= 1
        for col in range(right, left - 1, -1):
            answer.append(matrix[bottom][col])
        bottom -= 1
        for row in range(bottom, top - 1, -1):
            answer.append(matrix[row][left])
        left += 1
    
    return answer[:m * n]

# print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
