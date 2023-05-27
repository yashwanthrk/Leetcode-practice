class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphanumeric_string = ""
        for c in s:
            if c.isalnum():
                alphanumeric_string += c
        return alphanumeric_string == alphanumeric_string[::-1]

