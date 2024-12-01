# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        start = 1
        result = -1
        
        while (start <= n):
            
            mid = (start + n) // 2

            if isBadVersion(mid) == False:
                start = mid + 1

            else:
                result = mid
                n = mid - 1

        return result