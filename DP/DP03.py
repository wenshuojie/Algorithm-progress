# 300. 最长递增子序列

from cmath import pi
from typing import List

class Solution_v1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums) # 定义：dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

class Solution_v2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        top = [0] * len(nums)
        piles = 0

        for i in range(len(nums)):
            poker = nums[i]

            # 二分查找，要放在最左侧的堆
            left, right = 0, piles
            while left < right:
                mid = left + (right - left) // 2
                if top[mid] > poker:
                    right = mid
                elif top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid
            
            if left == piles:
                piles += 1

            top[left] = poker

        return piles


