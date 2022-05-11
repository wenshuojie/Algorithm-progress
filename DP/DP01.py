# 509. 斐波那契数

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp_i_1, dp_i_2 = 1, 0 # i-1 and i-2
        for _ in range(2, n+1):
            dp_i = dp_i_1 + dp_i_2
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i

        return dp_i_1