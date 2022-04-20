# 503. 下一个更大元素 II

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]: # nums是循环数组
        n = len(nums)
        stack = []
        res = [0] * n
        
        for i in range(2*n-1,-1,-1):
            while stack and nums[i % n] >= stack[-1]:
                stack.pop()

            res[i % n] = stack[-1] if stack else -1
            stack.append(nums[i % n])

        return res

solution = Solution()
print(solution.nextGreaterElements(nums = [1,2,3,4,3]))

