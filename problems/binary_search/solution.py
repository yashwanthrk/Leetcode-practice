class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
    
        while low <= high:
   
            mid = (high + low) // 2

            if target == nums[mid]:
                return mid

            elif target < nums[mid]:
                
                high = mid - 1
            else:
                low = mid + 1
        return -1
        
        