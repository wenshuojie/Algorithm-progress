# 最小覆盖子串

from collections import defaultdict
import math

class Solution:
    def minWindow(self , S: str, T: str) -> str:
        need = defaultdict(int) # 传入int：key不存在默认为int的默认值0
        win = defaultdict(int)
        for c in T:
            need[c] += 1
        
        left, right = 0, 0
        valid = 0 # 如果 valid 和 need.size 的大小相同，则说明窗口已满足条件
        start, lenth = 0, math.inf # 记录子串的起始位置

        while right < len(S):
            # 扩大窗口
            c = S[right]
            right += 1
            if c in need.keys():
                win[c] += 1
                if win[c] == need[c]:
                    valid += 1
            
            # 判断是否要缩小窗口
            while valid == len(need):
                # 更新结果
                if right-left < lenth:
                    start = left
                    lenth = right - left

                c = S[left]
                left += 1
                # if c in need.keys():
                #     win[c] -= 1
                #     if win[c] != need[c]: # !=的情况有两种：肯定是大于等于，只有判断才减valid
                #         valid -= 1

                if c in need.keys():
                    if win[c] == need[c]:
                        valid -= 1
                    win[c] -= 1
                    

        return S[start:start+lenth] if lenth != math.inf else ''

solution = Solution()        
print(solution.minWindow('AAACAAAB', 'ABC'))