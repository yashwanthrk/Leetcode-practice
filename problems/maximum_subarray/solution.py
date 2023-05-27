import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #  striver video
        
        
        # Get the minimum integer value
        max_value = -sys.maxsize - 1
        current_sum = 0

        for num in nums:
            current_sum += num
            
            # discard if it reaches negative, we dont need negative sub array
            if current_sum < 0:
                current_sum = 0

            max_value = max(max_value, current_sum)

    
        return max_value if max_value > 0 else max(nums)


        # dp = [0] * len(nums)
        # dp[0] = nums[0]

        # for i in range(1, len(nums)):
        #     dp[i]  = max(dp[i-1] + nums[i], nums[i])
        #     # print(dp)
        # return max(dp)

        

        







            