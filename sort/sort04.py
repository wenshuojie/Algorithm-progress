# 215. 数组中的第K个最大元素

from typing import List
import heapq
import random

class Solution_v1: # 小顶堆（小顶堆就是“筛子”）
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, num)
            while len(pq) > k:
                heapq.heappop(pq)

        return pq[0]

class Solution_v2: # 快速排序的应用
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.shuffle(nums)
        left, right = 0, len(nums)-1
        k = len(nums) - k # 第k个最大的元素==升序排列后的下标为len(nums)-k的元素
        while left <= right:
            p = self.partition(nums, left, right)
            if p < k:
                left = p+1
            elif p > k:
                right = p-1
            else:
                return nums[p]
        return -1

    def shuffle(self, nums):
        length = len(nums)
        for i in range(length):
            cInd = random.randint(i, length-1)
            nums[i], nums[cInd] = nums[cInd], nums[i]

    def partition(self, nums, left, right):
        pivot = nums[left]
        i, j = left+1, right
        while i <= j:
            while nums[i] <= pivot and i < right:
                i += 1
            while nums[j] > pivot and j > left:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        nums[left], nums[j] = nums[j], nums[l]
        return j
        




