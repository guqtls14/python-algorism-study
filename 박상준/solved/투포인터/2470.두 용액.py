"""
 *packageName    : 
 * fileName       : 2470.두 용액
 * author         : ipeac
 * date           : 2022-10-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-05        ipeac       최초 생성
 """
# n 전체 용액의 수
# n = 5
n = int(input())
# 용액리스트
# arr = [-2, 4, -99, -1, 98]
arr = list(map(int, input().split()))
# 0 에 가까운 용액을 만들어낸다.
# 두 용액을 섞을 수 있다.
arr.sort()

len_arr = len(arr)

start = 0
end = len_arr - 1

answer = abs(arr[start] + arr[end])

final = [arr[start], arr[end]]
while start < end:
    left_val = arr[start]
    right_val = arr[end]
    
    sum = left_val + right_val
    
    if abs(sum) < answer:
        answer = abs(sum)
        final = [left_val, right_val]
        if answer == 0:
            break
    if sum < 0:
        start += 1
    else:
        end -= 1
print(*final)
