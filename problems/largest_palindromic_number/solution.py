class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        
        from collections import Counter
        
        count = Counter(num)
        
        half = []
        middle = ""
        
        # Sort digits from 9 to 0 for maximizing the palindrome
        for digit in sorted(count.keys(), reverse=True):
            
            if digit == '0' and not half:
                # Skip leading zeros if no other digits are in the half
                continue
            
            if count[digit] >= 2:
                # Add half of the pairs to the half list
                half.append(digit * (count[digit] // 2))
            
            # Check for middle element
            if count[digit] % 2 == 1 and middle == "":
                middle = digit
        
        # Form the half palindrome and then the full palindrome
        half_palindrome = "".join(half)
        # Reverse the half to mirror it
        largest_palindrome = half_palindrome + middle + half_palindrome[::-1]
        
        # If the result is empty, return "0"
        if not largest_palindrome:
            return "0"
        
        # Remove leading zeros, except if the result is empty
        largest_palindrome = largest_palindrome.lstrip('0')
        
        # If stripping zeros results in an empty string, the largest palindrome is "0"
        return largest_palindrome if largest_palindrome else "0"