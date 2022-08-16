# 找到字符串中所有字母异位词

from collections import defaultdict
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        win, need = defaultdict(int), defaultdict(int)
        left, right = 0, 0
        valid = 0
        res = []

        for c in p:
            need[c] += 1
        
        while right < len(s):
            c = s[right]
            right += 1
            if c in need.keys():
                win[c] += 1
                if win[c] == need[c]:
                    valid += 1
            
            while right-left >= len(p):
                if valid == len(need):
                    res.append(left)
                c = s[left]
                left += 1
                if c in need.keys():
                    if win[c] == need[c]:
                        valid -= 1
                    win[c] -= 1
        return res

solution = Solution()
print(solution.findAnagrams(s = "cbaebabacd", p = "abc"))
print(solution.findAnagrams(s = "abab", p = "ab"))
