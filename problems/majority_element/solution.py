class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_ele = len(nums)//2
        nums.sort()
        return nums[majority_ele]