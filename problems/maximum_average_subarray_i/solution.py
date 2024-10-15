class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_window_sum = sum(nums[:k])
        current_window_sum = max_window_sum
        
        for i in range(k, len(nums)):
            # Slide the window to the right
            current_window_sum += nums[i] - nums[i - k]
            max_window_sum = max(max_window_sum, current_window_sum)
        
        # Return the maximum average
        return max_window_sum / k