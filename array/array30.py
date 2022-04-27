# 42. 接雨水

from turtle import right
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        l_max = r_max = 0

        res = 0
        while left < right:
            l_max = max(height[left], l_max)
            r_max = max(height[right],r_max)

            if l_max < r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1

        return res

solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))