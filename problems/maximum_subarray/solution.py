class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # # Get the minimum integer value
        # max_value = -sys.maxsize - 1
        # current_sum = 0

        # for num in nums:
        #     current_sum += num
            
        #     # discard if it reaches negative, we dont need negative sub array
        #     if current_sum < 0:
        #         current_sum = 0

        #     max_value = max(max_value, current_sum)

    
        # return max_value if max_value > 0 else max(nums)



        max_value = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_value = max(max_value, current_sum)

        return max_value