# 合并区间

from typing import List

class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b

class Solution:
    def merge(self , intervals: List[Interval]) -> List[Interval]:
        # write code here
        intervals.sort(key=lambda x:x.start)
        res = []
        for interval in intervals:
            if not res or interval.start > res[-1].end:
                res.append(interval)
            else:
                res[-1].end = max(res[-1].end, interval.end)
        return res