# 15. 三数之和

from typing import List

class Solution:
    def threeSum(self, nums, target: int):
        nums.sort()

        res = []
        i = 0
        while i < len(nums):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            val = nums[i]
            twotarget = target - val
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sums = nums[left] + nums[right]
                left_val = nums[left]
                right_val = nums[right]
                if sums == twotarget:
                    res.append([val, nums[left], nums[right]])
                    while nums[left] == left_val and left < right:
                        left += 1
                    while nums[right] == right_val and left < right:
                        right -= 1
                elif sums < twotarget:
                    while nums[left] == left_val and left < right:
                        left += 1
                elif sums > twotarget:
                    while nums[right] == right_val and left < right:
                        right -= 1
            i += 1
        return res

solution = Solution()
print(solution.threeSum([0,0,0],0))
print(solution.threeSum([-1,0,1,2,-1,-4],0))



