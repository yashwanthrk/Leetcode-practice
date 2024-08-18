class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
     
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if target == nums[i] + nums[j]:
        #             return [i, j]


        # return [-1, -1]

        num_dict = {}
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [i, num_dict[target - num]]
            else:
                num_dict[num] = i

        return [-1, -1]

           


