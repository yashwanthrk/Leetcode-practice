class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        subset = []
        visited = set()
        
        self.make_permutes(result, subset, visited, nums)
        return result
        
    def make_permutes(self, result, subset, visited, nums):
        print(subset, nums)
        if len(subset) == len(nums):
            result.append(subset)
            return
        
        for index in range(0, len(nums)):
            if index not in visited:
                visited.add(index)
                self.make_permutes(result, subset + [nums[index]], visited, nums)
                visited.remove(index)
                print(visited)

