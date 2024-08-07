class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphanumeric_chars = [c for c in s if c.isalnum()]
        alphanumeric_string = ''.join(alphanumeric_chars)
        return alphanumeric_string == alphanumeric_string[::-1]
