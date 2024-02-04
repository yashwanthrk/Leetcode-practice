class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            temp_max = 0
            for d in range(1, k + 1):
                if i - d < 0:
                    break
                temp_max = max(temp_max, arr[i - d])
                dp[i] = max(dp[i], dp[i - d] + temp_max * d)
        return dp[-1]