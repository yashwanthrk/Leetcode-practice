class Solution:
    def rob(self, nums: List[int]) -> int:

    

        # [58, 59, 77,  2, 82, 83, 50, 89, 34, 99, 24, 30, 44, 43, 58, 18, 88, 48, 15, 33]


        if not nums: 
            return 0
        
        if len(nums) == 1: 
            return nums[0]
        
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            # print(nums[i], dp[i-2], dp[i-1])

            # no adjacent houses; 
            # either max of not adjacent, or take big number
            
            # nums[k] = max(k + nums[k-2], nums[k-1])

            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            # print(dp[i])

        return dp[-1] 
     

        

