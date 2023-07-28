class Solution:
    def searchRange(self, nums, target):
        def binarySearch(nums, target, first):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target or (first and target == nums[mid]):
                    right = mid
                else:
                    left = mid + 1
            return left

        first = binarySearch(nums, target, True)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        last = binarySearch(nums, target, False)
        return [first, last-1]
