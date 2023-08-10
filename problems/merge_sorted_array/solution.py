class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
      
       # Pointers for nums1 and nums2
      p1 = m - 1
      p2 = n - 1
      
      # Pointer for merged nums1
      curr = m + n - 1
      
      # While there are still elements to compare
      while p1 >= 0 and p2 >= 0:
          if nums1[p1] < nums2[p2]:
              nums1[curr] = nums2[p2]
              p2 -= 1
          else:
              nums1[curr] = nums1[p1]
              p1 -= 1
          curr -= 1
      
      # If there are still elements in nums2
      while p2 >= 0:
          nums1[curr] = nums2[p2]
          p2 -= 1
          curr -= 1

      



