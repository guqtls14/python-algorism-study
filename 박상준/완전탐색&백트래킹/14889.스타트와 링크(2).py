"""
 *packageName    : 
 * fileName       : 14889.스타트와 링크(2)
 * author         : ipeac
 * date           : 2022-09-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-29        ipeac       최초 생성
 """
from itertools import combinations

n = int(input())
# n 개의 줄에 s
s = [list(map(int, input().split())) for _ in range(n)]
# 두팀의 능력치의 차를 최소로.
n_arr = set(i for i in range(n))
min_diff = 10e9
for combi in combinations(n_arr, n // 2):
    link = combi
    # 나머지는 스타트팀일거임
    start = list(set(n_arr) - set(link))
    link_sum = 0
    start_sum = 0
    
    for index in range(n // 2):
        for index2 in range(index + 1, n // 2):
            link_sum += s[start[index]][start[index2]] + s[start[index2]][start[index]]
            start_sum += s[link[index]][link[index2]] + s[link[index2]][link[index]]
    diff = abs(start_sum - link_sum)
    print(f"diff : {diff}")
    
    min_diff = min_diff if min_diff < diff else diff

print(min_diff)
