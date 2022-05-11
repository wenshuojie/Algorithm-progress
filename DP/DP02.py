# 322. 零钱兑换

from typing import List
import math

class Solution_v1: # 超出时间限制
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.dp(coins, amount)

    def dp(self, coins, amount):
        # base case
        if amount < 0:
            return -1
        if amount == 0:
            return 0

        res = math.inf
        for coin in coins:
            subProblems = self.dp(coins, amount-coin) # 子问题
            if subProblems == -1:
                continue
            res = min(res, subProblems+1) # +1：原问题在子问题基础上要拿一枚硬币

        return res if not res == math.inf else -1

class Solution_v2: # 自底向上
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1) # 定义：目标金额为i，需要dp[i]枚硬币（用amount+1填充）

        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i-coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if not dp[amount] == amount + 1 else -1