class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


    #    left = 0 
    #    while right < len(nums)):
           
    #        if nums[right] >= target:
    #            return 1
            
    #         if nums[right] + nums[left] < target:
    #             right += 1

    #         if nums[right] + nums[left] > target
    #             return 

        current_max = nums[0]

        if current_max >= target:
            return 1
            
        result = float("inf")
        left = 0
        for right in range(1, len(nums)):
            current_max += nums[right]
            while current_max >= target:
                result = min(right - left + 1, result)
                current_max -= nums[left]
                left += 1

          
        return 0 if result == float("inf") else result