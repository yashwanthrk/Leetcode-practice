class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort() 
        valid_triangle_count = 0
        
        for largest_side in range(len(nums) - 1, 1, -1):
            left, right = 0, largest_side - 1
            while left < right:
                # If the sum of the smaller sides is greater than the largest side, it's a valid triangle
                if nums[left] + nums[right] > nums[largest_side]:
                    # Count all valid pairs between left and right
                    valid_triangle_count += right - left  
                    right -= 1 
                else:
                    left += 1  

        return valid_triangle_count  # Ret