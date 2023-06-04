class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

    # "Find 2 numbers in the array that are equal and are at most k apart from each other."?

        
        hash_table = {}
        for index, num in enumerate(nums):
            if num in hash_table:
                old_index = hash_table[num]
                # print(hash_table)
                if abs(index - old_index) <= k:
                    return True
                else:
                    hash_table[num] = index
            else:
                hash_table[num] = index


        
        return False