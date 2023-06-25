class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        
        output = -1

        while i < j:
            sum = nums[i] + nums[j]
            if sum < k:
                output = max(output, nums[i] + nums[j])
                i += 1
            else:
                j -= 1

        return output

