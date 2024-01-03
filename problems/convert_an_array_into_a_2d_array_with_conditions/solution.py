class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        num_map = {} 
        result = [[]]  

        for num in nums:
            if num in num_map:
                num_map[num] += 1
                # If the current count is greater than the number of rows, add a new row
                if len(result) < num_map[num]:
                    result.append([])  

                # Append the number to the appropriate row based on its count
                result[num_map[num] - 1].append(num)  
            else:
                num_map[num] = 1
                result[0].append(num) 

        return result






        