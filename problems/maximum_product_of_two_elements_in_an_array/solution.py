class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        x, y = heapq.nlargest(2, nums)
        return (x-1) * (y-1)