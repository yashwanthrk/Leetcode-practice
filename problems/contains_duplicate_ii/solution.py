class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        from collections import defaultdict

        groups = defaultdict(list)

        for index, num in enumerate(nums):
            groups[num].append(index)
        
        for index_list in groups.values():
            for index in range(1, len(index_list)):
                if abs(index_list[index] - index_list[index - 1]) <= k:
                    return True
        
        return False