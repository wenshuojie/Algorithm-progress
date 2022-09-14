import heapq

class MedianFinder:

    def __init__(self):
        self.small = [] # 大顶堆
        self.large = [] # 小顶堆

    def addNum(self, num: int) -> None:
        if len(self.small) < len(self.large):
            heapq.heappush(self.large, num)
            heapq.heappush(self.small, -heapq.heappop(self.large))
        else:
            heapq.heappush(self.small, -num)
            heapq.heappush(self.large, -heapq.heappop(self.small))

    def findMedian(self) -> float:
        if len(self.large) < len(self.small):
            return -self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2