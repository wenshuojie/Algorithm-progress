# 数组中的逆序对

from typing import List

class Solution:
    mod = 1000000007
    def InversePairs(self , data: List[int]) -> int:
        self.temp = [None] * len(data)
        self.res = 0
        self.sort(data, 0, len(data)-1)
        return self.res % self.mod

    def sort(self, data, left, right):
        if left >= right:
            return
        
        mid = left + (right - left) // 2
        self.sort(data, left, mid)
        self.sort(data, mid+1, right)
        self.merge(data, left, mid, right)
    
    def merge(self, data, left, mid, right):
        for i in range(left, right+1):
            self.temp[i] = data[i]

        i, j = left, mid+1
        for k in range(left, right+1):
            if i > mid: # 必须先判断区间情况
                data[k] = self.temp[j]
                j += 1
            elif j > right:
                data[k] = self.temp[i]
                i += 1
                self.res += j - (mid+1)
            elif self.temp[i] > self.temp[j]:
                data[k] = self.temp[j]
                j += 1
            else:
                data[k] = self.temp[i]
                i += 1
                self.res += j - (mid+1)

solution = Solution()
print(solution.InversePairs([7,2,45,7689,1,3]))
