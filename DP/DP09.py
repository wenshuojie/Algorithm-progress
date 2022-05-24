# 583. 两个字符串的删除操作

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        common = self.longestCommonSubsequence(word1, word2)
        return len(word1)-common+len(word2)-common 

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

solution = Solution()
print(solution.minDistance(word1 = "sea", word2 = "eat"))