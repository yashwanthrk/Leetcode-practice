class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        for _ in range(k):
            min_index = nums.index(min(nums))
            nums[min_index] = nums[min_index] * multiplier
            
        return nums

