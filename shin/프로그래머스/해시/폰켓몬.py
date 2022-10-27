# def solution(nums):
#     unique = len(set(nums))

#     if len(nums) / 2 > unique:
#         return unique
#     else:
#         return len(nums) / 2


from itertools import combinations

def solution(arr):
    arr1=len(set(arr))
  
    if len(arr)//2 >= arr1:
        return arr1
    else:
        return len(arr)//2


# arr=[3,1,2,3]
# arr=[3,3,3,2,2,2]
arr=[3,1,2,3]
print(solution(arr))