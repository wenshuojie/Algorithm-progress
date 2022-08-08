# 315. 计算右侧小于当前元素的个数
from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]
        
        temp = [None] * size
        res = [0] * size
        index = [i for i in range(size)]

        self.sort(nums, 0, size-1, temp, res, index)
        return res
        # 换成这个也可以实现归并排序：排序坐标也可以实现归并排序
        # return [nums[i] for i in index]

    def sort(self, nums, l ,r, temp, res, index):
        if l == r:
            return

        mid = l + (r - l) // 2
        self.sort(nums, l, mid, temp, res, index)
        self.sort(nums, mid+1, r, temp, res, index)
        self.merge(nums, l, mid, r, temp, res, index)
        

    def merge(self, nums, l, mid, r, temp, res, index):
        for i in range(l, r+1):
            temp[i] = index[i]

        i , j = l, mid+1
        for k in range(l, r+1):
            if i > mid:
                index[k] = temp[j]
                j += 1
            elif j > r:
                index[k] = temp[i]
                i += 1
                res[index[k]] += r - mid
            elif nums[temp[i]] <= nums[temp[j]]:
                index[k] = temp[i]
                i += 1
                res[index[k]] += (j - mid - 1)
            else:
                index[k] = temp[j]
                j += 1

solution = Solution()
print(solution.countSmaller([7,2,45,7689,1,3]))

class Solution_v3:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.temp = [None] * len(nums)
        self.index = [i for i in range(len(nums))]
        self.res = [0] * len(nums)
        self.sort(nums, 0, len(nums)-1)
        return self.res

    def sort(self, nums, left, right):
        if left >= right:
            return
        
        mid = left + (right - left) // 2
        self.sort(nums, left, mid)
        self.sort(nums, mid+1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        for i in range(left, right+1):
            self.temp[i] = self.index[i]
        
        i, j = left, mid+1
        for k in range(left, right+1):
            if i > mid:
                self.index[k] = self.temp[j]
                j += 1
            elif j > right:
                self.index[k] = self.temp[i]
                i += 1
                self.res[self.index[k]] += (j - (mid+1))
            elif nums[self.temp[i]] < nums[self.temp[j]]:
                self.index[k] = self.temp[i]
                i += 1
                self.res[self.index[k]] += (j - (mid+1))
            else:
                self.index[k] = self.temp[j]
                j += 1
                

solution_v3 = Solution_v3()
print(solution_v3.sortArray([7,2,45,7689,1,3]))
