# 二维数组中的查找

from typing import List

class Solution:
    def Find(self , target: int, array: List[List[int]]) -> bool:
        row, col = len(array), len(array[0])
        if row == 0 or col == 0:
            return False
        i, j = row-1, 0
        while i >= 0 and j <= col-1:
            if target > array[i][j]:
                j += 1
            elif target < array[i][j]:
                i -= 1
            else:
                return True

        return False

