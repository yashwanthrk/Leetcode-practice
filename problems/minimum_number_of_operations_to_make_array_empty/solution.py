class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        num_maps = {}

        for num in nums:
            num_maps[num] = num_maps.get(num, 0) + 1
        
        operations = 0


        for num, value in num_maps.items():
            if value == 1:
                return -1
                
            operations += (value // 3)
            if (value % 3 != 0):
                operations += 1

        return operations