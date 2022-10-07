"""
 *packageName    : 
 * fileName       : 2805.나무 자르기
 * author         : ipeac
 * date           : 2022-10-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-07        ipeac       최초 생성
 """
import bisect

# n, m = map(int, input().split())
n, m = 4, 7
tree_height = [20, 15, 10, 17]
# tree_height = list(map(int,input().split()))
tree_height.sort()
start = 0
end = max(tree_height)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for tree in tree_height:
        if tree > mid:
            cnt += tree - mid
    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
