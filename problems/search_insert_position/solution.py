class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = ((i + j) // 2)

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return i

            

                