from collections import defaultdict

class Solution: # 496. 下一个更大元素 I
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = self.getNextLarge(nums2)
        return [res[i] for i in nums1]

    def getNextLarge(self, nums):
        res = defaultdict(int)
        ass_stack = [] # 单调栈
        
        for i in range(len(nums)-1, -1, -1):
            while ass_stack and ass_stack[-1] <= nums[i]:
                ass_stack.pop()
            
            res[nums[i]] = ass_stack[-1] if ass_stack else -1
            ass_stack.append(nums[i])
        
        return res

class Solution: # 739. 每日温度
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        ass_stack = []

        for i in range(len(temperatures)-1, -1, -1):
            while ass_stack and temperatures[ass_stack[-1]] <= temperatures[i]:
                ass_stack.pop()
            
            res[i] = ass_stack[-1]-i if ass_stack else 0
            ass_stack.append(i)
        
        return res

class Solution: # 503. 下一个更大元素 II
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ass_stack = [] # 单调栈
        len_nums = len(nums)
        res = [0] * len_nums

        for i in range(2*len(nums)-1, -1, -1):
            while ass_stack and ass_stack[-1] <= nums[i % len_nums]:
                ass_stack.pop()
            
            res[i % len_nums] = ass_stack[-1] if ass_stack else -1
            ass_stack.append(nums[i])
        
        return res