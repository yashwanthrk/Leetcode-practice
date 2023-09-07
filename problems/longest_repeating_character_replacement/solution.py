class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}  
        result = 0      
        left = 0        
        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1  # Update the count of the current character.

            # the condition (r - l + 1) - max(count.values()) > k is checking whether the difference between the size of the current window and the maximum count of any character within the window exceeds the allowed number of replacements k.
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1  
                # Shrink the window by moving the left pointer.
                left += 1

            result = max(result, right - left + 1)  
        return result