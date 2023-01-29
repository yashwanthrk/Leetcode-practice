class Solution:
    def climbStairs(self, n: int) -> int:
        
        # if not n:
        #     return 0
            
        # if n == 1 or n == 2:
        #     return n

        # for i in range( n-2):
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)

        if not n:
            return 0

        if n == 1:
            return 1
            
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]   
                