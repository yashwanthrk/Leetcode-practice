class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        first_max = float(-inf)
        second_max = float(-inf)

        for num in nums:
            if num > first_max:
                second_max = first_max
                first_max = num
            
            elif num > second_max:
                second_max = num
        
        return (first_max - 1) * (second_max - 1)
        