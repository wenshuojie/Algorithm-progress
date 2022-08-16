# 寻找左,右侧边界的二分搜索

from typing import List

class Solution:
    def searchL(self , nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid - 1
        
        if left == len(nums):
            return -1
        
        return left if nums[left] == target else -1
    
    def searchR(self , nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        
        if right < 0:
            return -1
        return right if nums[right] == target else -1

solution = Solution()
print(solution.searchL([1,2,2,2,3,3],2))
print(solution.searchR([1,2,2,2,3,3],2))