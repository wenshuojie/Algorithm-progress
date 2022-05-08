# 912. 排序数组（快速排序）

from random import random
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.shuffle(nums)
        self.sort(nums, 0, len(nums)-1)
        return nums

    def sort(self, nums, l ,r):
        if l >= r:
            return

        p = self.partition(nums, l, r)
        self.sort(nums, l, p-1)
        self.sort(nums, p+1, r)

    def partition(self, nums, l, r):
        pivot = nums[l]
        i, j = l+1, r
        while i <= j:
            while i < r and nums[i] <= pivot:
                i += 1 # 此 while 结束时恰好 nums[i] > pivot
            while j > l and nums[j] > pivot:
                j -= 1 # 此 while 结束时恰好 nums[j] <= pivot

            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        
        nums[l], nums[j] = nums[j], nums[l]
        return j

    # 洗牌算法
    def shuffle(self,nums):
        size = len(nums)
        for i in range(size):
            index = random.randint(i, size-1)
            nums[i], nums[index] = nums[index], nums[i]