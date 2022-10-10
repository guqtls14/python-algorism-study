"""
 *packageName    : 
 * fileName       : 2512.예산
 * author         : ipeac
 * date           : 2022-10-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-06        ipeac       최초 생성
 """
import bisect

n = 4
budget = [120, 110, 140, 150]
total_budget = 485
budget.sort()
start = 0
end = budget[-1]

psum = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    psum[i] = psum[i - 1] + budget[i - 1]

while start <= end:
    mid = (start + end) // 2
    point = bisect.bisect_left(budget, mid)
    total_sum = psum[point] + mid * (n - point)
    
    if total_sum > total_budget:
        end = mid - 1
    else:
        start = mid + 1
print(end)
