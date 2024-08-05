class Solution:
    def climbStairs(self, n: int) -> int:
       
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2

        prev1, prev2 = 1, 2
        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current

        return prev2