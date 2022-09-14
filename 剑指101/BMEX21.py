# 239. 滑动窗口最大值

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ass_queue = []
        window = []
        res = [0] * len(nums)

        for i in range(len(nums)):
            window.append(nums[i])
            if i < k-1:
                while ass_queue and ass_queue[-1] < nums[i]:
                    ass_queue.pop()
                ass_queue.append(nums[i])
            else:
                while ass_queue and ass_queue[-1] < nums[i]:
                    ass_queue.pop()
                ass_queue.append(nums[i])

                res.append(ass_queue[0])

                num = window.pop(0)
                if num == ass_queue[0]:
                    ass_queue.pop(0)
        return res


from collections import deque # 使用双端队列实现单调队列，快很多

class ass_queue:
    def __init__(self) -> None:
        self.ass_queue = deque()
    
    def push(self, num):
        while self.ass_queue and self.ass_queue[-1] < num:
            self.ass_queue.pop()
        self.ass_queue.append(num)

    def pop(self, n):
        if n == self.ass_queue[0]:
            self.ass_queue.popleft()
    
    def get_max(self):
        if self.ass_queue:
            return self.ass_queue[0]

class Solution_v2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = ass_queue() # 单调队列
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