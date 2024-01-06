class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:


        i = 0
        j = len(nums) - 1
        k = len(nums) - 1

        sorted_nums = [-1] * (len(nums))
        
        while i <= j and k > -1:
            if nums[i] ** 2 > nums[j] ** 2:
                sorted_nums[k] = nums[i] ** 2
                i += 1
            elif nums[i] ** 2 <= nums[j] ** 2:
                sorted_nums[k] = nums[j] ** 2
                j -= 1
            k -= 1

        return sorted_nums