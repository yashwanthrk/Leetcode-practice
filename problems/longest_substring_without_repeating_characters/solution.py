class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # https://www.youtube.com/watch?v=FCbOzdHKW18&ab_channel=GregHogg

        if not s:
            return 0

        left = 0
        visited = set()
        max_len = 0

        for right, ch in enumerate(s):

            while ch in visited:
                visited.remove(s[left])
                left += 1
            
            max_len = max(max_len, right - left + 1)
            visited.add(ch)

        return max_len


    # def is_unique(s, start, end):
    # # Set to check for uniqueness of characters
    #     chars = set()
        
    #     for i in range(start, end + 1):
    #         if s[i] in chars:
    #             return False
    #         chars.add(s[i])
        
    #     return True

    # def lengthOfLongestSubstring(s):
    #     n = len(s)
    #     max_length = 0
        
    #     # Loop over each character as the starting point
    #     for i in range(n):
    #         # Try every possible end point from i
    #         for j in range(i, n):
    #             # Check if substring from i to j has all unique characters
    #             if is_unique(s, i, j):
    #                 max_length = max(max_length, j - i + 1)
        
    #     return max_length