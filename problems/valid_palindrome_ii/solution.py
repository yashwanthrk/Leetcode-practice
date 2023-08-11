class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        p1, p2 = 0, len(s) - 1
        
        while p1 < p2:
            if s[p1] != s[p2]:
                return isPalindrome(s[p1+1:p2+1]) or isPalindrome(s[p1:p2])
            p1 += 1
            p2 -= 1
            
        return True
