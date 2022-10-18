import sys

input = sys.stdin.readline
n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 사각형의 크기를 구합니다.
def calc_rec_size(x1, y1, x2, y2):
    return abs(x2 - x1 + 1) * abs(y2 - y1 + 1)

def check(x1, y1, x2, y2):
    return all([  # all 은 iterable 안의 모든 데이터가 참인 경우에만 참 반환(and)
        grid[i][j] > 0
        for i in range(x1, x2 + 1)
        for j in range(y1, y2 + 1)
    ])

pass
# 시뮬레이션을 돈다.
max_size = -1

def simulate():
    global max_size
    for row in range(n):
        for col in range(m):
            
            if grid[row][col] > 0:  # 그리드가 양수인 경우에만 루프
                for i in range(row, n):
                    for j in range(col, m):
                        if check(row, col, i, j):
                            # 모두 양수인경우
                            size = calc_rec_size(row, col, i, j)
                            max_size = max(max_size, size)
    
    return max_size

print(simulate())