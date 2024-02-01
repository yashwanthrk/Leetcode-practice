class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:


        if len(nums) % 3 != 0:
            return []
        
        # Sort the numbers
        nums.sort()

        result = []

        for i in range(0, len(nums), 3):
            if i + 2 < len(nums):
                # If the difference between the maximum and minimum elements in the subarray is greater than k, return an empty list
                if nums[i + 2] - nums[i] > k:
                    return []
            
                result.append([nums[i], nums[i + 1], nums[i + 2]])

        return result
