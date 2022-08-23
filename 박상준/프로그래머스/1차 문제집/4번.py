"""





"""

"""
동전을 뒤집기 위하여 같은 줄 모든 동전을 뒤집어야함
초기 상태에서 최소 몇 번의 동전을 뒤집어야 목표 상태가 되는지

행, 열 둘다 뒤집을 수 있음

목표 상태를 만들지 못하는 경우 -1 반환

1 ≤ beginning의 길이 = target의 길이 ≤ 10

비트마스킹?
"""


def check(beginning, target, row_bit, col_bit):
    ROW, COL = len(beginning), len(beginning[0])
    for row in range(ROW):
        for col in range(COL):
            if row_bit % (1 << row):


def solution(beginning, target):
    print(f"beginning : {beginning}")
    print(f"target : {target}")
    answer = 0
    ROW, COL = len(beginning), len(beginning[0])
    
    for row_bit in range(1 << ROW):
        for col_bit in range(1 << COL):
            # check
            if True:
    
    return answer


solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]],
         [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])
