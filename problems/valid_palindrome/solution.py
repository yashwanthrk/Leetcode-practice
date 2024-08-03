class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        # alphanumeric_chars = [c for c in s if c.isalnum()]
        # alphanumeric_string = ''.join(alphanumeric_chars)
        # return alphanumeric_string == alphanumeric_string[::-1]


        # Removing white spaces 
        s = "".join(s.split()).lower()

    
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
