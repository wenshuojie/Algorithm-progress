# 410. 分割数组的最大值

'''
思路同array18，可以看作
每个货物的重量是nums[i]，
运送m天，求最小的载重量
'''
from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums) + 1

        while left < right:
            mid = left + (right - left) // 2
            if self.f(nums,mid) <= m:
                right = mid
            else: 
                left = mid + 1
        
        return left

        
    def f(self,nums:List[int],max:int) -> int:
        sums = 0
        m = 0
        for num in nums:
            if sums + num > max:
                sums = num
                m += 1
            else:
                sums += num
        return m + 1

solution = Solution()
print(solution.splitArray(nums = [7,2,5,10,8], m = 2))
