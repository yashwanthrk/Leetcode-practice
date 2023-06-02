class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Using shifting pointers with P1 is the most left side of the array and P2 is the most right side of the array.
        p1 = 0
        p2 = len(height) - 1


        max_area = 0
        while p1 < p2:
            height_size = min(height[p1], height[p2])
            weight = p2 - p1 
            # current_area = min(height[p1], height[p2]) * (p2 - p1)
            current_area = height_size * weight
            max_area = max(max_area, current_area)   

            if height[p1] < height[p2]:
                p1 += 1

            # both are same
            # elif height[p1] > height[p2]:
            #     p2 -= 1

            # else:
            #     p2 -= 1
            # both are same
            else:
                p2 -= 1

        return max_area


        # # brute force
        # height_len = len(height)
        # max_area = 0
        # for i in range(height_len - 1):
        #     for j in range(i, height_len):
        #         current_area = min(height[i], height[j]) * (j - i)
        #         max_area = max(max_area, current_area)
        # return max_area