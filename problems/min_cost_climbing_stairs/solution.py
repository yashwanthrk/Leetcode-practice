class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        
        dp = [0] * len(cost)

        dp[0] = cost[0]
        dp[1] = cost[1]

        for index in range(2, len(cost)):
            print(dp[index - 2] + cost[index],  dp[index - 1], index)
            dp[index] = min(dp[index - 2] + cost[index], dp[index - 1] + cost[index] )
            print(dp[index])
        # print(dp)
        return dp[-1] if dp[-1] < dp[-2] else dp[-2]