# 875. 爱吃香蕉的珂珂

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) + 1
        
        while left < right:
            mid = left + (right - left) // 2
            if self.spendhours(piles,mid) == h:
                right = mid
            elif self.spendhours(piles,mid) > h:
                left = mid + 1
            elif self.spendhours(piles,mid) < h: # 花费的hours小，说明速度v大了，搜索区间左移
                right = mid

        return left

    def spendhours(self,piles:List[int],x:int) -> int: # 函数关系：速度x(根/小时)，f(x)花费的时间
        hours = 0
        for pile in piles:
            hours += pile // x
            if (pile % x > 0):
                hours += 1
        return hours

solusion = Solution()
print(solusion.minEatingSpeed([3,6,7,11],8))
print(solusion.minEatingSpeed([30,11,23,4,20],5))
print(solusion.minEatingSpeed([30,11,23,4,20],6))



    