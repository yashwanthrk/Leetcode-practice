class Solution:
    def arraySign(self, nums: List[int]) -> int:
    
        def signFucn(x):

            if x > 0:
                return 1

            elif x < 0:
                return -1

            else:
                return 0

        product = nums[0]
        
        for i in range(1, len(nums)):
            product *= nums[i]
        
        return signFucn(product)