"""
 *packageName    : 
 * fileName       : 2417.정수 제곱근
 * author         : ipeac
 * date           : 2022-10-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-06        ipeac       최초 생성
 """
n = int(input())
left = 0
right = n
while left <= right:
    mid = (left + right) // 2
    if mid ** 2 < n:
        left = mid + 1
    else:
        right = mid - 1
print(left)
