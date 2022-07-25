"""
 *packageName    : 
 * fileName       : 1051_숫자 정사각형_S4
 * author         : jihye94
 * date           : 2022-07-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-25        jihye94       최초 생성
 """
# 세로 가로

n, m = map(int, input().split())
rac = [list(map(int, input())) for _ in range(n)]

min_value = n if n < m else m
max_value = -1
for i in range(n):
    for j in range(m):
        for k in range(min_value):
            if i + k < n and j + k < m:

                if rac[i][j] == rac[i + k][j] == rac[i][j + k] == rac[i + k][j + k]:
                    if max_value < (k + 1) ** 2:
                        max_value = (k + 1) ** 2

print(max_value)
