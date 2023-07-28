class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(result, [], nums, 0)
        return result

    def backtrack(self, result, subset, nums, start):
        

        # deep copy
        result.append(subset[:])

        for i in range(start, len(nums)):
            
            subset.append(nums[i])
            self.backtrack(result, subset, nums, i + 1)
            
            subset.pop()

    