# 1143. 最长公共子序列

from typing import List

class Solution_v1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.dp(text1, 0, text2, 0)
    
    # 计算s1[i..]和s2[j..]的最长公共子序列长度
    def dp(self, text1, i, text2, j):
        # base case
        if i == len(text1) or j == len(text2):
            return 0

        if text1[i] == text2[j]:
            return self.dp(text1, i+1, text2, j+1) + 1
        else:
            return max(
                # self.dp(text1, i+1, text2, j+1),
                self.dp(text1, i, text2, j+1),
                self.dp(text1, i+1, text2, j)
            )

solution = Solution_v1()
print(solution.longestCommonSubsequence(text1 = "abcde", text2 = "ace"))

# 备忘录
class Solution_v2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.memo = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        return self.dp(text1, 0, text2, 0)
    
    # 计算s1[i..]和s2[j..]的最长公共子序列长度
    def dp(self, text1, i, text2, j):
        # base case
        if i == len(text1) or j == len(text2):
            return 0

        if self.memo[i][j] != -1:
            return self.memo[i][j]

        if text1[i] == text2[j]:
            self.memo[i][j] = self.dp(text1, i+1, text2, j+1) + 1
        else:
            self.memo[i][j] = max(
                # self.dp(text1, i+1, text2, j+1),
                self.dp(text1, i, text2, j+1),
                self.dp(text1, i+1, text2, j)
            )
        
        return self.memo[i][j]

solution = Solution_v2()
print(solution.longestCommonSubsequence(text1 = "abcde", text2 = "ace"))

# 自底向上
class Solution_v3:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_text1 = len(text1)
        len_text2 = len(text2)

        # 定义：s1[0..i-1] 和 s2[0..j-1] 的 lcs 长度为 dp[i][j]
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1, len_text1+1):
            for j in range(1, len_text2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]

solution = Solution_v3()
print(solution.longestCommonSubsequence(text1 = "abcde", text2 = "ace"))

