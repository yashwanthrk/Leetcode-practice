class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)

        left = [1] * len(nums)
        right = [1] * len(nums)
        result = [1] * len(nums)
      
        for index in range(1, length):
            left[index] = nums[index - 1] * left[index -1]


        for index in range(len(nums) - 2, -1, -1):
            right[index] = nums[index + 1] * right[index + 1]

        for index in range(length):
            result[index] = left[index] * right[index]

        return result