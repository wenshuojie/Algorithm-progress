# 167. 两数之和 II

from typing import List

class Solution:
    def twoSum_v1(self, numbers: List[int], target: int) -> List[int]: # 返回第几个数，且假定只有一组满足target
        # numbers:非递减顺序排列 
        left = 0
        right = len(numbers) - 1
        while left <= right:
            sums = numbers[left] + numbers[right]
            if sums == target:
                return [left+1, right+1]
            elif sums < target:
                left += 1
            elif sums > target:
                right -= 1
        
        return [-1, -1]

    def twoSum_v2(self, numbers: List[int], target: int) -> List[int]: # 返回全部的无重复的具体数字
        numbers.sort() # 数组先排序，可用双指针
        left = 0
        right = len(numbers) - 1
        result = []
        while left <= right:
            sums = numbers[left] + numbers[right]
            left_val = numbers[left]
            right_val = numbers[right]
            if sums == target:
                result.append([numbers[left],numbers[right]])
                # left += 1
                # right -= 1
                while numbers[left] == left_val and left <= right:
                     left += 1
                while numbers[right] == right_val and left <= right:
                    right -= 1
            elif sums > target:
                # right -= 1
                while numbers[right] == right_val and left <= right:
                    right -= 1
            elif sums < target:
                # left += 1
                while numbers[left] == left_val and left <= right:
                     left += 1

        return result

solution = Solution()
print(solution.twoSum_v2(numbers = [1,3,1,2,2,3], target = 4))
print(solution.twoSum_v2(numbers = [1,1,1,2,2,3,3], target = 4))








