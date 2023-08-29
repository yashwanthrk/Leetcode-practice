class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        p0, curr, p2 = 0, 0, len(nums) - 1


        while curr <= p2:
            print(nums)

            # curr traverses the entire array. If it finds a 0, it swaps it with the number at p0 and moves both pointers (curr and p0) forward. 

            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
                    
                # If it finds a 2, it swaps it with the number at p2 and only moves p2 backward (since the number swapped to curr could be a 0, 1, or 2 and needs to be checked again). If curr finds a 1, it just moves forward.

            elif nums[curr] == 2:

                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1

                # dont decrment curr here


            else:
                curr += 1
