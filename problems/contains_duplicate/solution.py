class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        counter_num = Counter(nums)
        
        for num in nums:
            if counter_num[num] > 1:
                return True
        
        return False