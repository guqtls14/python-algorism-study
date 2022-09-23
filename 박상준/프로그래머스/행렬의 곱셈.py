"""
 *packageName    : 
 * fileName       : 행렬의 곱셈
 * author         : qkrtkdwns3410
 * date           : 2022-09-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-12        qkrtkdwns3410       최초 생성
 """

def product_matrix(X, Y):
    answer = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return answer

def solution(arr1, arr2):
    return product_matrix(arr1, arr2)

# solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])
solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]])
