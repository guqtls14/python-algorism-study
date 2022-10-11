"""
 *packageName    : 
 * fileName       : 1. Two Sum
 * author         : ipeac
 * date           : 2022-10-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-10        ipeac       최초 생성
 """
import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        
        for i in range(len(nums)):
            if nums[i] in hash:
                return [hash[nums[i]], i]
            
            hash[target - nums[i]] = i

print(Solution.twoSum(None, nums=[2, 7, 11, 15], target=9))
# print(Solution.twoSum(None, nums=[3, 2, 4], target=6))
# print(Solution.twoSum(None, nums=[3, 3], target=6))
