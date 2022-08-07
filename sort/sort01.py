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

solution = Solution()
print(solution.sortArray([1,2,3,44,5,6,2,3]))