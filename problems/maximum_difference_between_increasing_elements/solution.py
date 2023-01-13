class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        max_value = -1
        min_value = nums[0]

        for i in range(1, len(nums)):
            min_value = min(min_value, nums[i])
            max_value = max(nums[i] - min_value, max_value)

        return max_value if max_value != 0 else -1