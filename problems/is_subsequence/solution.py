class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
         


        if not s:
            return True
                
        s_i = 0
        for t_i in t:
            if s[s_i] == t_i:
                s_i += 1
            if s_i == len(s):
                return True
        
        return s_i == len(s)


        # # copied leetcode discussions 
        # LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        # i = 0
        # j = 0

        # while i < LEFT_BOUND and j < RIGHT_BOUND:
        #     # move both pointers or just the right pointer
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1

        # return i == LEFT_BOUND