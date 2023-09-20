class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    
        max_window = sum(nums[:k])
        max_window_avg = max_window / k
        for i in range(1, len(nums) - k  + 1):
            curr_window = max_window - nums[i - 1] + nums[i + k - 1]
            max_window = curr_window
            max_window_avg = max(max_window_avg, curr_window / k)
        
        return max_window_avg



        # n = len(nums)
        # curr = 0
        
        # for i in range(k):
        #     curr += nums[i]
        
        # ans = curr
        
        # for i in range(k, n):
        #     curr += (nums[i] - nums[i-k])
        #     if ans < curr:
        #         ans = curr
        
        # return (ans/k)