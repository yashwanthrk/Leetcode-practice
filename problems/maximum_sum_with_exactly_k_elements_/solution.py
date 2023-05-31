class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_ele = max(nums)

        result = 0
        while k > 0:
            result += max_ele
            max_ele += 1
            k -= 1
            
        return result