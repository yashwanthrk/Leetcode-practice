class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    #   copied from Neetcode


        char_set = set()
        left_index = 0

        result = 0
        for right_index in range(len(s)):
            while s[right_index] in char_set:
                char_set.remove(s[left_index])
                left_index += 1

            char_set.add(s[right_index])

            result = max(result, right_index - left_index + 1)
            
        return result
                    
                
        