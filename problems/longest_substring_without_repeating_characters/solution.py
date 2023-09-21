class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        left = 0
        max_len = 0
        char_set = set()
        
        for right, ch in enumerate(s):
            while ch in char_set:  
                # Keep removing characters from the left until the current character is not in the set
                char_set.remove(s[left])
                left += 1
            char_set.add(ch)
            max_len = max(max_len, right - left + 1)  
        
        return max_len