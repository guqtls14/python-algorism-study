"""
 *packageName    : 
 * fileName       : 1654.랜선자르기
 * author         : ipeac
 * date           : 2022-10-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-06        ipeac       최초 생성
 """
from statistics import median

k, n = 4, 11
lan = [802, 743, 457, 539]
print(sum(lan) // 4)

lan.sort()
left = 1
right = max(lan)
while left <= right:
    mid = (left + right) // 2
    lines = 0
    for i in lan:
        lines += i // mid
    if lines >= n:
        left = mid + 1
    else:
        right = mid - 1
print(right)
