# 528. 按权重随机选择

from random import random
from typing import List

class Solution:
    def __init__(self, w: List[int]):
        self.presum = [0]
        for num in w:
            self.presum.append(self.presum[-1]+num)
            
    def pickIndex(self) -> int:
        lenth = len(self.presum)
        if lenth == 1:
            return -1

        target = random.randint(1,self.presum[-1])
        left,right = 0,lenth
        while left<right:
            mid = left + (right-left) // 2
            if self.presum[mid] == target:
                right = mid
            elif self.presum[mid] > target:
                right = mid
            elif self.presum[mid] < target:
                left = mid + 1

        return left-1 # 这里的-1是因为前缀和数组与原数组有1位的偏移

