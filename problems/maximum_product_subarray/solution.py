class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        max_product = min_product = result = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            # Calculate the potential max and min products at the current position
            if num < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)
            
            result = max(result, max_product)
        
        return result