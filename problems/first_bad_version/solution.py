# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 1
        res = -1
        while (i <= n):
            mid = ( i + n ) // 2
            if isBadVersion(mid) == False:
                i = mid + 1
            else:
                res = mid
                n = mid - 1
        return res
            

                
