class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        count = [0, 0, 0] 

        for num in nums:
            count[num] += 1

        RED, WHITE, BLUE = count

        nums[:RED] = [0] * RED
        nums[RED: RED + WHITE] = [1] * WHITE
        nums[RED + WHITE:] = [2] * BLUE
        