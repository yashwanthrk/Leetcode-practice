class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
    
        nums.sort()
        previous_elements_sum = 0

        result = -1

        for num in nums:
            if num < previous_elements_sum:
                result = num + previous_elements_sum
            previous_elements_sum += num
            
        return result