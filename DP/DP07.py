# 53. 最大子数组和

from typing import List

class Solution_v1:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return

        dp = [0]*len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])

        return max(dp)

solution = Solution_v1()
print(solution.maxSubArray(nums = [5]))


# 优化空间（当前状态只与前一个状态相关）
class Solution_v2:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return

        res = nums[0]
        pre = 0
        for i in range(len(nums)):
            pre = max(nums[i], pre+nums[i])
            res = max(res, pre)

        return res

solution = Solution_v2()
print(solution.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))

        

