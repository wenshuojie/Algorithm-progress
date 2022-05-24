# 712. 两个字符串的最小ASCII删除和 tip：ord()：返回Ascii码

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        self.memo = [[-1]*len(s2) for _ in range(len(s1))] 
        return self.dp(s1, 0, s2, 0)
    
    def dp(self, s1, i, s2, j):
        res = 0
        # base case
        if i == len(s1):
            while j < len(s2):
                res += ord(s2[j])
                j += 1
            return res
        if j == len(s2):
            while i < len(s1):
                res += ord(s1[i])
                i += 1
            return res
        
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        
        if s1[i] == s2[j]:
            self.memo[i][j] = self.dp(s1, i+1, s2, j+1)
        else:
            self.memo[i][j] = min(
                ord(s1[i]) + self.dp(s1, i+1, s2, j),
                ord(s2[j]) + self.dp(s1, i, s2, j+1)
            )
        return self.memo[i][j]


