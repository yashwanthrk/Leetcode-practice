class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        total = sum(nums)
        target = total - x
        
        if target == 0:
            return len(nums)
        
        left, right = 0, 0
        current_sum = 0
        max_length = float('-inf')
        
        while right < len(nums):
            current_sum += nums[right]
            right += 1
            
            while current_sum > target and left < right:
                current_sum -= nums[left]
                left += 1
            
            if current_sum == target:
                max_length = max(max_length, right - left)
        
        return len(nums) - max_length if max_length != float('-inf') else -1
