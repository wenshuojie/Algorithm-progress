# 304. 二维区域和检索 - 矩阵不可变

from scipy.fftpack import cc_diff


class NumMatrix:
    def __init__(self, matrix):
        self.row = len(matrix)
        self.col = len(matrix[0])
        if self.row == 0 and self.col == 0:
            return
        self.presum = [[0]*(self.col+1) for i in range(self.row+1)]
        for i in range(1,self.row+1):
            for j in range(1,self.col+1):
                self.presum[i][j] = self.presum[i][j-1] + self.presum[i-1][j] + matrix[i-1][j-1] -self.presum[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.presum[row2+1][col2+1] - self.presum[row1][col2+1] - self.presum[row2+1][col1] + self.presum[row1][col1]