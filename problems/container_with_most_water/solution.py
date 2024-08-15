class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # think it as recantangular
        # rectangle with a height given by the shorter line and a width given by the distance 
        # between the lines. Return the area of the rectangle with the largest area
        
        p1 = 0
        p2 = len(height) - 1
        
        max_area = 0
        
        while p1 < p2:
            
            left_height = height[p1]
            right_height = height[p2] 

            height_size = min(left_height, right_height)
            weight = p2 - p1 
            
            current_area = height_size * weight
            max_area = max(max_area, current_area)   

            if left_height < right_height:
                p1 += 1
            else:
                p2 -= 1

        return max_area