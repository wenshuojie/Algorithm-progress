# 239. 滑动窗口最大值

from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = MonotonicQueue() # 单调队列
        res = []

        for i in range(len(nums)):
            if i < k-1:
                # 先填满window前k-1
                window.push(nums[i])
            else:
                window.push(nums[i])
                res.append(window.max())
                window.pop(nums[i-k+1])

        return res

class MonotonicQueue:
    def __init__(self) -> None:
        self.queue = deque()

    def push(self,x):
        while self.queue and self.queue[-1] < x:
            self.queue.pop()
        self.queue.append(x)

    def max(self):
        if self.queue:
            return self.queue[0]
        return None

    def pop(self,x):
        if x == self.queue[0]:
            self.queue.popleft()

solution = Solution()
print(solution.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))

