class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

    
        if not s:
            return 0

        unique_str = set()
        max_str_len = 0
        left = 0

        for right, ch in enumerate(s):

            while ch in unique_str:
                unique_str.remove(s[left])
                left += 1
            
            unique_str.add(ch)
            
            max_str_len = max(right - left + 1, max_str_len)

        return max_str_len
                    
