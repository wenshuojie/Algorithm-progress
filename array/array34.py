# 54. 螺旋矩阵
# 59. 螺旋矩阵 II

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        up, down = 0, m-1
        left, right = 0, n-1

        res = []
        while True:
            for i in range(left, right+1):
                res.append(matrix[up][i])
            up += 1
            if up > down:
                break

            for i in range(up, down+1):
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
            down -= 1
            if down < up:
                break
            
            for i in range(down, up-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return res

    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        up, down = 0, n-1
        left, right = 0, n-1

        num = 1
        while True:
            for i in range(left, right+1):
                res[up][i] = num
                num += 1
            up += 1
            if up > down:
                break

            for i in range(up, down+1):
                res[i][right] = num
                num += 1
            right -= 1
            if left > right:
                break

            for i in range(right, left-1, -1):
                res[down][i] = num
                num += 1
            down -= 1
            if up > down:
                break

            for i in range(down, up-1, -1):
                res[i][left] = num
                num += 1
            left += 1
            if left > right:
                break
        return res


