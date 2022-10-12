"""
 *packageName    : 
 * fileName       : 14889.스타트와 링크
 * author         : ipeac
 * date           : 2022-10-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-12        ipeac       최초 생성
 """
from itertools import combinations

n = int(input())
sc = [list(map(int, input().split())) for _ in range(n)]
# sc = [[0, 1, 2, 3, 4, 5], [1, 0, 2, 3, 4, 5], [1, 2, 0, 3, 4, 5], [1, 2, 3, 0, 4, 5], [1, 2, 3, 4, 0, 5], [1, 2, 3, 4, 5, 0]]
score = set(i for i in range(n))
min_diff = 1e9
for combi in combinations(score, n // 2):
    # print("==========================================")
    start = combi
    link = list(set(score) - set(start))
    sum, sum2 = 0, 0
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            if i == j: continue
            # print("==========================================")
            # print(i)
            # print(j)
            sum += sc[start[i]][start[j]] + sc[start[j]][start[i]]
            sum2 += sc[link[i]][link[j]] + sc[link[j]][link[i]]
    min_diff = min_diff if min_diff < abs(sum - sum2) else abs(sum - sum2)

print(min_diff)
