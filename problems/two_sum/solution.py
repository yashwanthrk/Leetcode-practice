class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for index, num in enumerate(nums):
            if num in num_dict:
                return [index, num_dict[num]]
            else:
                num_dict[target - num] = index
        return []