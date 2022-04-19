# 739. 每日温度

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            res[i] = stack[-1]-i if stack else 0
            stack.append(i)

        return res

solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))
print(solution.dailyTemperatures([30,40,50,60]))

            