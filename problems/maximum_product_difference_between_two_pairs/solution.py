class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:


        first_max = float('-inf')
        second_max = float('-inf')

        first_min = float('inf')
        second_min = float('inf')


        for num in nums:

            if num > first_max:
                second_max = first_max
                first_max = num

            elif num > second_max:
                second_max = num

            if num < first_min:
                second_min = first_min
                first_min = num

            elif num < second_min:
                second_min = num

        
        return  (first_max * second_max) - (first_min * second_min)

        
            