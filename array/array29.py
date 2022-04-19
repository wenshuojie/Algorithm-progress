# 5. 最长回文子串

from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            res1 = self.centerPalindrome(s,i,i) # 奇数中心
            res2 = self.centerPalindrome(s,i,i+1) # 偶数中心
            res = res1 if len(res1) > len(res) else res
            res = res2 if len(res2) > len(res) else res

        return res

    def centerPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return s[left+1:right]

solution = Solution()
print(solution.longestPalindrome("babad"))
