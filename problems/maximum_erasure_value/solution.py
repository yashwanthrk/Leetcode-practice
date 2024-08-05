class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        

        if not nums:
            return 0

        left = 0
        max_score = current_sum = 0
        unique_nums = set()
        for right in range(0, len(nums)):
            
            while nums[right] in unique_nums:
                unique_nums.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            
            # Add the current number to the set and update the current sum
            unique_nums.add(nums[right])
            current_sum += nums[right]

            max_score = max(max_score, current_sum)


        return max_score


