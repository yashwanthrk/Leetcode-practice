class Solution:
    def longestPalindrome(self, s: str) -> str:


        result_len = 0
        start, end = 0, 0

        for i in range(len(s)):

            #  odd string
            l , r = i, i
            # while pointer is still in bound and palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if ( (r - l) + 1 ) > result_len:
                    start = l
                    end = r
                    result_len = max((r-l)  + 1, result_len)
                l -= 1
                r += 1

            l , r = i, i + 1
            #  even string
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if ( (r - l) + 1 ) > result_len:
                    start = l
                    end = r
                    result_len = max((r-l)  + 1, result_len)
                l -= 1
                r += 1

        return s[start: end + 1]



            

