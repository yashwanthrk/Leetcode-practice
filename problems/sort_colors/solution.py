class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # color_dict = {}
        # for num in nums:
        #     color_dict[num] = color_dict.get(num, 0) + 1
        
        # for key, value in color_dict.items():
        #     for j in range(value):
        #         nums.append(key)
        #         nums.pop(0)


        # i = 0 
        # j = len(nums) - 1

        # while i <= j:
        #     if nums[i] >= nums[j]:
        #         nums[i], nums[i+1] = nums[i+1], nums[i]
        #         i += 1
        #     else:

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
            

        
                





        
        
