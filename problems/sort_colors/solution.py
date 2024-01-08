class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        p0, p2 = 0, len(nums) - 1
        curr = 0

        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
        
        # If nums[curr] == 2, 
        # it swaps it with the number at p2 and only moves p2 backward (since the number swapped to curr could be a 0, 1, or 2 and needs to be checked again). If curr finds a 1, it just moves forward.

            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
                
            else:
                curr += 1