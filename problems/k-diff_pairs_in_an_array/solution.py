class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
       
        if k < 0:
            return 0  
        
        num_map = Counter(nums)  
        k_pairs = 0

        for num in num_map:
            if k == 0:
                # Check if there are duplicates for k == 0
                if num_map[num] > 1:
                    k_pairs += 1
            else:
                # Check if num + k exists in the map
                if num + k in num_map:
                    k_pairs += 1
        
        return k_pairs