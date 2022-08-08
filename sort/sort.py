from typing import List


class Solution_v4:
    def countSmaller(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]
        
        temp = [None] * size
        index = [i for i in range(size)]

        self.sort(nums, 0, size-1, temp, index)
        return [nums[i] for i in index]

    def sort(self, nums, l ,r, temp, index):
        if l == r:
            return

        mid = l + (r - l) // 2
        self.sort(nums, l, mid, temp, index)
        self.sort(nums, mid+1, r, temp, index)
        self.merge(nums, l, mid, r, temp, index)
        

    def merge(self, nums, l, mid, r, temp, index):
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
            elif nums[temp[i]] <= nums[temp[j]]:
                index[k] = temp[i]
                i += 1
            else:
                index[k] = temp[j]
                j += 1

            # if nums[temp[i]] <= nums[temp[j]]:
            #     index[k] = temp[i]
            #     i += 1
            # elif nums[temp[i]] > nums[temp[j]]:
            #     index[k] = temp[j]
            #     j += 1
            # elif i > mid:
            #     index[k] = temp[j]
            #     j += 1
            # else: 
            #     index[k] = temp[i]
            #     i += 1

solution_v4 = Solution_v4()
print(solution_v4.countSmaller([8,4,8,2,5,0,6]))