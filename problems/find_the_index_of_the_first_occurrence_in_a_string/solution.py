class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        h  = 0
        h_len = len(haystack)
        
        n = 0 
        n_len = len(needle)

        while h < h_len:
       
            
            if haystack[h] == needle[n]:
                n += 1
            else:
                h = h - n
                n = 0

            h += 1

            if n == n_len:
                return  h - n

        return -1