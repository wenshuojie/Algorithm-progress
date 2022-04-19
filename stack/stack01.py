# 496. 下一个更大元素 I
from collections import defaultdict
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic_res = defaultdict(int)
        stack = [] # 单调栈
        
        for i in range(len(nums2)-1,-1,-1): # 倒着入栈，因为要观察后面的数
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            dic_res[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        
        return [dic_res[i] for i in nums1]

solution = Solution()
print(solution.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
