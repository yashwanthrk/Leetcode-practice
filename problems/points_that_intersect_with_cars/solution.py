class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        

        seen = set()
        
        for start, end in nums:
            for num in range(start, end + 1):
                seen.add(num)
        
        return len(seen)