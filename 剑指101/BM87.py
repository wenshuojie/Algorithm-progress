# 合并两个有序的数组

class Solution:
    def merge(self , A, m, B, n):
        temp_A = A.copy()

        i, j = 0, 0
        for k in range((m+n)):
            if i >= m:
                A[k] = B[j]
                j += 1
            elif j >= n:
                A[k] = temp_A[i]
                i += 1
            elif temp_A[i] > B[j]:
                A[k] = B[j]
                j += 1
            else:
                A[k] = temp_A[i]
                i += 1