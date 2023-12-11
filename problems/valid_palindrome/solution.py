class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = "".join(s.split()).lower()
        
        if not s:
            return True

        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
        
        return True
