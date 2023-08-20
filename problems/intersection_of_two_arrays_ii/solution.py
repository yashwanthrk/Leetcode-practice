

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq_map = {}
        common_list = []

        # Populate the frequency map with elements from nums1
        for num in nums1:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Iterate through nums2 and find common elements
        for num in nums2:
            if num in freq_map and freq_map[num] > 0:
                common_list.append(num)
                freq_map[num] -= 1

        return common_list
