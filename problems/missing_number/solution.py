class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        num_total = sum(nums)
        for i in range(n + 1):
            num_total -= i
        return abs(num_total)
                