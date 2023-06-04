class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        current_max = nums[0]

        if current_max >= target:
            return 1

        # positive infinity
        result = float("inf")
        # Comparing with other numbers
        # print(inf_value > 10)  # Output: True
        # print(inf_value < 100)  # Output: False

        left = 0
        for right in range(1, len(nums)):
            current_max += nums[right]
            
            while current_max >= target:
                result = min(right - left + 1, result)
                current_max -= nums[left]
                left += 1

          
        return 0 if result == float("inf") else result