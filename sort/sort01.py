# 912. 排序数组（归并排序）

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.sort(nums, 0, len(nums)-1)
        return nums

    def sort(self, nums, l ,r):
        if l >= r: # 或者：l == r
            return

        mid = l + (r - l) // 2
        self.sort(nums, l, mid)
        self.sort(nums, mid+1, r)

        # 合并
        temp = []
        i, j = l, mid+1
        while i <= mid or j <= r:
            # if i > mid or (j <= r and nums[i] > nums[j]):
            #     temp.append(nums[j])
            #     j += 1
            # else:
            #     temp.append(nums[i])
            #     i += 1

            # 或者：
            if j > r or (i <= mid and nums[i] < nums[j]):
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        nums[l: r+1] = temp

# solution = Solution()
# print(solution.sortArray([1,2,3,44,5,6,2,3]))


class Solution_v2:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.temp = [None] * len(nums)
        self.sort(nums, 0, len(nums)-1)
        return nums

    def sort(self, nums, left, right):
        # base case
        if left >= right:
            return
        
        # 分
        mid = left + (right - left) // 2
        self.sort(nums, left, mid)
        self.sort(nums, mid+1, right)

        # 合
        self.merge(nums, left, mid, right)
    
    def merge(self, nums, left, mid, right):
        for i in range(left, right+1):
            self.temp[i] = nums[i]
        
        i, j = left, mid+1
        for k in range(left, right+1):
            if i == mid+1:
                nums[k] = self.temp[j]
                j += 1
            elif j == right+1:
                nums[k] = self.temp[i]
                i += 1
            elif self.temp[i] < self.temp[j]:
                nums[k] = self.temp[i]
                i += 1
            else:
                nums[k] = self.temp[j]
                j += 1

# solution_v2 = Solution_v2()
# print(solution_v2.sortArray([8,4,8,2,5,0,6]))

class Solution_v3:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.temp = [None] * len(nums)
        self.index = [i for i in range(len(nums))]
        self.sort(nums, 0, len(nums)-1)
        return [nums[i] for i in self.index]

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
            elif nums[self.temp[i]] < nums[self.temp[j]]:
                self.index[k] = self.temp[i]
                i += 1
            else:
                self.index[k] = self.temp[j]
                j += 1

solution_v3 = Solution_v3()
print(solution_v3.sortArray([8,4,8,2,5,0,6]))