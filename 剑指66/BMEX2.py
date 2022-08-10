# 字符串的排列

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        valid = 0
        win, need = defaultdict(int), defaultdict(int)
        for c in s1:
            need[c] += 1

        while right < len(s2):
            # 扩大窗口
            c = s2[right]
            right += 1
            if c in need.keys():
                win[c] += 1
                if win[c] == need[c]:
                    valid += 1

            # 判断要不要缩小窗口
            while right-left >= len(s1):
                if valid == len(need):
                    return True
                
                c = s2[left]
                left += 1
                if c in need.keys():
                    if win[c] == need[c]:
                        valid -= 1
                    win[c] -= 1
                
        return False

solution = Solution()
print(solution.checkInclusion('ab','eidboaoo'))
print(solution.checkInclusion('ab','eidbaooo'))               


