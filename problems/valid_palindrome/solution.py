class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        character_list = [c.lower() for c in s if c.isalnum()]
        clean_str = ""
        
        for c in character_list:
            clean_str += c

        i = 0
        j = len(clean_str) - 1

        while i <= j:
            if clean_str[i] != clean_str[j]:
                return False
            
            i += 1
            j -= 1

        return True