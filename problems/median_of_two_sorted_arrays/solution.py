class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)
        
        new_arr = [0] * (m + n)
        
        i = 0
        j = 0
        k = 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                new_arr[k] = nums1[i]
                k += 1
                i += 1
            else:
                new_arr[k] = nums2[j]
                k += 1
                j += 1
        
        while i < m:
            new_arr[k] = nums1[i]
            k += 1
            i += 1
        
        while j < n:
            new_arr[k] = nums2[j]
            k += 1
            j += 1

        
        print(new_arr)

        if len(new_arr) % 2 != 0:
            return new_arr[len(new_arr) // 2]
        else:
            median = (new_arr[len(new_arr)//2 - 1] + new_arr[len(new_arr)//2]) / 2
            return median

            