# 315. 计算右侧小于当前元素的个数
from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]
        
        temp = [None] * size
        res = [0] * size
        index = [i for i in range(size)]

        self.sort(nums, 0, size-1, temp, res, index)
        return res

    def sort(self, nums, l ,r, temp, res, index):
        if l == r:
            return

        mid = l + (r - l) // 2
        self.sort(nums, l, mid, temp, res, index)
        self.sort(nums, mid+1, r, temp, res, index)
        self.merge(nums, l, mid, r, temp, res, index)
        

    def merge(self, nums, l, mid, r, temp, res, index):
        for i in range(l, r+1):
            temp[i] = index[i]

        i , j = l, mid+1
        for k in range(l, r+1):
            if i > mid:
                index[k] = temp[j]
                j += 1
            elif j > r:
                index[k] = temp[i]
                i += 1
                res[index[k]] += r - mid
            elif nums[temp[i]] <= nums[temp[j]]:
                index[k] = temp[i]
                i += 1
                res[index[k]] += (j - mid - 1)
            else:
                index[k] = temp[j]
                j += 1

