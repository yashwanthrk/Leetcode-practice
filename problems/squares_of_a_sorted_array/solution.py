class Solution:
      def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []  
        left, right = 0, len(nums)-1  
        
        while left <= right:
            if nums[left] < 0:  
                # if the element pointed by left pointer is negative
                
                if abs(nums[left]) >= nums[right]:
                    res.append(nums[left]**2)  
                    left += 1  
                else:
                    res.append(nums[right]**2)  
                    right -= 1  
            else:  
                break
        
        # loop through the remaining elements from right pointer to left pointer and 
        # append their squares to the result array
        for i in range(right, left-1, -1):
            res.append(nums[i]**2)
        
         # reverse the result array to get the squares in non-decreasing order
        res.reverse() 
        return res