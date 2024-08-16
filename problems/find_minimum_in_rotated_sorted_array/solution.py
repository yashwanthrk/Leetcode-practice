class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        # sorted array
        if nums[0] < nums[-1]:
            return nums[0]
        

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            # Check if the mid element is the minimum
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            # Decide whether to go left or right
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return nums[l] 