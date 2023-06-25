class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
    
        # neetcode

        total = 0 
        for num in nums:
            total += num
        
        left_sum = 0

        for i, num in enumerate(nums):

            right_sum = total - nums[i] - left_sum

            if left_sum == right_sum:
                return i

            left_sum += num
            
        return -1
            

       
