class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0

        for e in range(len(nums)):
            if i == 0 or i == 1 or nums[i - 2] != nums[e]:
                nums[i] = nums[e]
                i += 1
        
        return i
        