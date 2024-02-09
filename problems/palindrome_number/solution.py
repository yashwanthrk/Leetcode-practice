class Solution:
    def isPalindrome(self, x: int) -> bool:

# If x ends with a 0 (x % 10 == 0) and x is not 0, 
# it cannot be a palindrome. 
# For example, 10, 20, 30, etc., are not palindromes since there's no leading zero to match the trailing zero.
        
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_num = 0
        original = x

        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return x == reversed_num or x == reversed_num // 10