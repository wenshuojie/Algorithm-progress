# 283. 移动零

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        length = self.removeElement(nums,0) # 先移除0，再在末尾补0
        for i in range(length,len(nums)):
            nums[i] = 0

    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow