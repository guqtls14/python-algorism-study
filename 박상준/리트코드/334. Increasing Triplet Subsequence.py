"""
 *packageName    : 
 * fileName       : 334. Increasing Triplet Subsequence
 * author         : ipeac
 * date           : 2022-10-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-11        ipeac       최초 생성
 """

def Solution(nums):
    first = second = float('inf')
    if len(nums) < 3:
        return False
    
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:  # n 이 첫번째와 두번째의 값 이하가 아닌 경우
            return True
    return False

# print(Solution([1, 2, 3, 4, 5]))
# print(Solution([20, 100, 10, 12, 5, 13]))
print(Solution([1, 5, 0, 4, 1, 3]))
# print(Solution([5, 4, 3, 2, 1]))
# print(Solution([2, 1, 5, 0, 4, 6]))
