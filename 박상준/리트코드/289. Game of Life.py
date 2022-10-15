"""
 *packageName    : 
 * fileName       : 289. Game of Life
 * author         : ipeac
 * date           : 2022-10-14
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-14        ipeac       최초 생성
 """
from typing import List

def gameOfLife(board: List[List[int]]) -> None:
    m = len(board[0])
    n = len(board)
    
    return board

# print(gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
print(gameOfLife([[1, 1], [1, 0]]))
