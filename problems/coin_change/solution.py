class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1

        dp = [amount + 1] * (amount + 1)
    
    
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
                    print(dp[a])
        return dp[amount] if dp[amount] != amount + 1 else -1
    
        