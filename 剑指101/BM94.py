# 接雨水问题

from typing import List

class Solution:
    def maxWater(self , arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        l_max, r_max = 0, 0
        res = 0

        while left < right:
            l_max = max(l_max, arr[left])
            r_max = max(r_max, arr[right])

            if arr[left] < arr[right]:
                res += min(l_max, r_max)-arr[left]
                left += 1
            else:
                res += min(l_max, r_max)-arr[right]
                right -= 1
        
        return res
