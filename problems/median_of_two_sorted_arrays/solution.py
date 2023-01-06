class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        merged_nums = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged_nums.append(nums1[i])
                i += 1 
            
            else:
                merged_nums.append(nums2[j])
                j += 1
   
                
        
        if i == len(nums1):
            merged_nums = merged_nums + nums2[j:]
        if j == len(nums2):
            merged_nums = merged_nums + nums1[i:]
        
        size = len(merged_nums)
        if size % 2 != 0:
            return merged_nums[(size // 2)]
        
        return (merged_nums[(size // 2)] + merged_nums[((size // 2) - 1)]) / 2
            
            