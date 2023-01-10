class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        num_dict = {}
        for index, num in enumerate(numbers):
            if num in num_dict:
                return [num_dict[num] + 1, index + 1]
            else:
                num_dict[target - num] = index
        return []

        