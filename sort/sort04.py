# 215. 数组中的第K个最大元素

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 小顶堆（小顶堆就是“筛子”）
        pq = []
        for num in nums:
            heapq.heappush(pq, num)
            while len(pq) > k:
                heapq.heappop(pq)

        return pq[0]
