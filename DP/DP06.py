# 72. 编辑距离

# class Solution_v1:
#     def minDistance(self, word1: str, word2: str) -> int:
#         len_s1 = len(word1)
#         len_s2 = len(word2)
#         return self.dp(word1, len_s1-1, word2, len_s2-1)

#     def dp(self, s1, i, s2, j):
#         # base case
#         if i == -1:
#             return j+1 # 走完s1，s2剩余字母需要添加到s1中
#         if j == -1:
#             return i+1 # 走完s2，s1中的剩余字母需要删除

#         if s1[i] == s2[j]:
#             return self.dp(s1, i-1, s2, j-1) # 字母相同则跳过

#         return min(
#             self.dp(s1, i, s2, j-1)+1,# 插入
#             self.dp(s1, i-1, s2, j)+1, # 删除
#             self.dp(s1, i-1, s2, j-1)+1 # 替换
#         )
# # Solution_v1存在重复子问题

# solution = Solution_v1()
# print(solution.minDistance(word1 = "horse", word2 = "ros"))
# print(solution.minDistance(word1 = "intention", word2 = "execution"))

class Solution_v2:
    def minDistance(self, word1: str, word2: str) -> int:
        len_s1 = len(word1)
        len_s2 = len(word2)
        # dp = [[0]*(len_s2+1)]*(len_s1+1) # 这样创建的list是对第一行的引用！！！
        dp = [[0 for _ in range(len_s2+1)] for _ in range(len_s1+1)] # 这才是开辟新空间

        # base case
        for i in range(len_s1+1):
            dp[i][0] = i

        for j in range(len_s2+1):
            dp[0][j] = j

        for i in range(1, len_s1+1):
            for j in range(1, len_s2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + 1,
                        dp[i][j-1] + 1,
                        dp[i-1][j-1] + 1
                    )
        
        return dp[len_s1][len_s2]

    def minDistance_v2(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 第一行
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j-1] + 1
        # 第一列
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i-1][0] + 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] ) + 1
        #print(dp)      
        return dp[-1][-1]

solution = Solution_v2()
print(solution.minDistance_v2(word1 = "", word2 = ""))
print(solution.minDistance(word1 = "", word2 = ""))

        
