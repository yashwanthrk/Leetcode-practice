class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        result_len = 0
        start, end = 0, 0

        def expand_around_center(l, r, start, end, result_len):
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result_len:
                    start = l
                    end = r
                    result_len = r - l + 1
                l -= 1
                r += 1
            return start, end, result_len

        for i in range(len(s)):
            # Odd-length palindrome
            start, end, result_len = expand_around_center(i, i, start, end, result_len)
            # Even-length palindrome
            start, end, result_len = expand_around_center(i, i + 1, start, end, result_len)

        return s[start: end + 1]