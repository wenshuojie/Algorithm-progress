# 295. 数据流的中位数

import heapq

class MedianFinder:

    def __init__(self):
        self.small = [] # 大顶堆
        self.large = [] # 小顶堆


    def addNum(self, num: int) -> None:
        # 维护1：元素相差不超过1
        # 维护2：large堆顶 >= small堆顶
        if len(self.small) >= len(self.large):
            heapq.heappush(self.small, -num)
            heapq.heappush(self.large, -(heapq.heappop(self.small)))
        else:
            heapq.heappush(self.large, num)
            heapq.heappush(self.small, -(heapq.heappop(self.large)))


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-(self.small[0])+self.large[0]) / 2

medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
medianFinder.addNum(3)
medianFinder.addNum(5)
print(medianFinder.findMedian())