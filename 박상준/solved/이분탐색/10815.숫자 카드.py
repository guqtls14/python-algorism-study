"""
 *packageName    : 
 * fileName       : 10815.숫자 카드
 * author         : ipeac
 * date           : 2022-10-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-06        ipeac       최초 생성
 """
n = 5
arr = [6, 3, 2, 10, -10]
m = 8
target = [10, 9, -5, 2, 3, 4, 5, -10]
arr.sort()
target.sort()

for value in target:
    start = 0
    end = len(arr) - 1
    flag = False
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < value:
            start = mid + 1
        elif arr[mid] > value:
            end = mid - 1
        else:
            flag = True
            print(1, end=" ")
            break
    
    if not flag:
        print(0, end=" ")
