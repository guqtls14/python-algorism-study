"""
 *packageName    : 
 * fileName       : 11053.가장 긴 증가한 수열
 * author         : ipeac
 * date           : 2022-09-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-24        ipeac       최초 생성
 """
# n = int(input())
# n_arr = list(map(int, input().split()))
#
n = int(input())
a = list(map(int, input().split(" ")))
d = [0] * n

for i in range(n):
    d[i] = 1
    for j in range(0, i):
        if a[j] < a[i] and d[i] < d[j] + 1:
            d[i] = d[j] + 1

print(max(d))
