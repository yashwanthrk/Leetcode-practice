class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
         
        common = set()

        for num1 in nums1:
            if num1 in nums2:
                common.add(num1)

        return common
