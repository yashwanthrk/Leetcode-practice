class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # copied leetcode discussions 
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        i = 0
        j = 0

        while i < LEFT_BOUND and j < RIGHT_BOUND:
            # move both pointers or just the right pointer
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == LEFT_BOUND