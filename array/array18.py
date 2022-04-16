# 1011. 在 D 天内送达包裹的能力

from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights) + 1
        while left < right:
            mid = left + (right - left) // 2
            if self.f(weights,mid) <= days:
                right = mid
            else:
                left = mid + 1
        
        return left


    def f(self, weights: List[int], maxw: int) -> int:
        days = 0
        sumweight = 0
        for weight in weights:
            if (sumweight + weight) > maxw:
                sumweight = weight
                days += 1
            else:
                sumweight += weight
        
        return days + 1 # +1:需要运走最后的货物

    # def f(self,weights,x):
    #     days = 0
    #     i = 0
    #     while(i < len(weights)):
    #         cap = x
    #         while i < len(weights):
    #             if cap < weights[i]:
    #                 break
    #             else:
    #                 cap -= weights[i]
    #                 i += 1
    #         days += 1

    #     return days

solution = Solution()
print(solution.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))
# print(solution.shipWithinDays([1,2,3,4,5,6,7,8,9,10],9))
print(solution.shipWithinDays([3,2,2,4,1,4],3))
print(solution.shipWithinDays([1,2,3,1,1],4))


