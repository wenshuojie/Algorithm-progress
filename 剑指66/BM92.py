# 最长无重复子数组

from typing import List
from collections import defaultdict
import math

class Solution:
    def maxLength(self , arr: List[int]) -> int:
        win = defaultdict(int)
        lenth = -math.inf
        left, right = 0, 0

        while right < len(arr):
            num = arr[right]
            right += 1
            win[num] += 1

            while win[num] > 1:
                win[arr[left]] -= 1
                left += 1
            
            lenth = max(lenth, right-left)
        
        return lenth
            


        
