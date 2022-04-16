# 26. 原地删除有序数组中的重复项

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        left, right = 0, 0
        while(right < len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            right += 1

        return left+1

solution = Solution()
print(solution.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))

