class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
      i = m - 1
      j = n - 1
      k = m + n - 1

      while j > -1:

        # Check if i is negative, which means all remaining nums1 elements have been checked

        if i < 0 or nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1
        k -= 1
    
