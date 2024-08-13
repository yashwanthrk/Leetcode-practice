class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        if k > len(nums):
            return 0


        max_sum = 0
        curr_sum = 0
        distinct_set = set()
        left = 0

        for right in range(len(nums)):
            
            while nums[right] in distinct_set:
                # Remove the leftmost element if it's a duplicate
                distinct_set.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            distinct_set.add(nums[right])
            curr_sum += nums[right]

            if right - left + 1 == k:
                max_sum = max(max_sum, curr_sum)
                # Slide the window by removing the leftmost element
                distinct_set.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

        return max_sum
