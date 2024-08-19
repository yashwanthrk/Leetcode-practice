class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        num_count = {}

        for num in nums1:
            num_count[num] = num_count.get(num, 0) + 1

        result = []

        for num in nums2:
            if num in num_count and num_count[num] > 0:
                result.append(num)
                num_count[num] -= 1

        return result