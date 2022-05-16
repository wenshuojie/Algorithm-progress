# 931. 下降路径最小和

from operator import le
from typing import List
import math

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        self.n = len(matrix)
        res = math.inf
        for j in range(self.n):
            self.memo = [[6666 for _ in range(self.n)] for _ in range(self.n)]
            res = min(res, self.dp_v2(matrix, self.n-1, j))
        return res

    '''
    dp定义：从第一行（matrix[0][..]）向下落，
    落到位置 matrix[i][j] 的最小路径和为 dp(matrix, i, j)
    '''

    # 暴力穷举解法，存在重叠子问题
    def dp_v1(self, matrix, i, j):
        if i >= self.n or i < 0 or j >= self.n or j < 0:
            return 99999

        # 第1行，base case
        if i == 0:
            return matrix[i][j]

        return matrix[i][j] + min(self.dp_v1(matrix,i-1,j-1),\
                                self.dp_v1(matrix, i-1, j),\
                                self.dp_v1(matrix, i-1, j+1))

    # 用备忘录的方法消除重叠子问题
    def dp_v2(self,matrix, i, j):
        
        if i >= self.n or i < 0 or j >= self.n or j < 0:
            return 99999

        if i == 0:
            return matrix[i][j]

        # 查找备忘录，防止重复计算
        if self.memo[i][j] != 6666:
            return self.memo[i][j]

        self.memo[i][j] = matrix[i][j] + min(self.dp_v2(matrix,i-1,j-1),\
                                self.dp_v2(matrix, i-1, j),\
                                self.dp_v2(matrix, i-1, j+1))

        return self.memo[i][j]

    # 自底向上
    def dp_v3(self, matrix, i ,j):
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    matrix[i][j] = min(matrix[i][j]+matrix[i-1][j], matrix[i][j]+matrix[i][j+1])
                elif j == n-1:
                    matrix[i][j] = min(matrix[i][j]+matrix[i-1][j], matrix[i][j]+matrix[i][j-1], matrix[i][j]+matrix[i][j+1])
                else:
                    matrix[i][j] = min(matrix[i][j]+matrix[i-1][j], matrix[i][j]+matrix[i][j-1])

        return min(matrix[n-1])

solution = Solution()
matrix_1 = [[2,1,3],[6,5,4],[7,8,9]]
matrix_2 = [[-19,57],[-40,-5]]
print(solution.minFallingPathSum(matrix_1))

        

