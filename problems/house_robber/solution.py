class Solution:
    def rob(self, nums: List[int]) -> int:
        

        # if not nums: 
        #     return 0
        
        # if len(nums) == 1: 
        #     return nums[0]
        
        # dp = [0] * len(nums)

        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     # print(nums[i], dp[i-2], dp[i-1])

        #     # no adjacent houses; 
        #     # either max of not adjacent, or take big number
            
        #     # nums[k] = max(k + nums[k-2], nums[k-1])

        #     dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        #     # print(dp[i])

        # return dp[-1] 


        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        # set prev1 to 0 as iteration starts from 2 nd element
        prev1, prev2 = 0, nums[0]

        for i in range(1, len(nums)):
            current = max(prev2, prev1 + nums[i])
            prev1, prev2 = prev2, current

        return prev2