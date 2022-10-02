"""
 *packageName    : 
 * fileName       : 14467.소가 길을 건너간 이유1
 * author         : ipeac
 * date           : 2022-10-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-02        ipeac       최초 생성
 """
from collections import defaultdict

m = int(input())
# arr = [[3, 1], [3, 0], [6, 0], [2, 1], [4, 1], [3, 0], [4, 0], [3, 1]]
arr = [list(map(int, input().split())) for _ in range(m)]
# print(f"arr : {arr}")

dic = defaultdict(lambda: -1)

cnt = 0

for lvalue in arr:
    if dic[lvalue[0]] != lvalue[1] and dic[lvalue[0]] != -1:
        cnt += 1
    dic[lvalue[0]] = lvalue[1]

print(cnt)
