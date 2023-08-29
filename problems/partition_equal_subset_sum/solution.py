class Solution:
   def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # Check if the total sum is odd, in which case equal partition is not possible
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        dp = set()
        dp.add(0)

        for num in nums:
            
            new_dp = set()
            for tar in dp:
                new_sum = tar + num
                if new_sum == target:
                    return True
                if new_sum < target:
                    new_dp.add(new_sum)

            dp.update(new_dp)
        
        return target in dp