class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_vowels_count, current_vowels_count = 0, 0

        # Set up the initial window and count
        for i in range(k):
            if s[i] in vowels:
                current_vowels_count += 1
        max_vowels_count = current_vowels_count


        
        # for index in range(1, len(s) - k + 1):
            # curr_window = s[index:index + k]
            
            # i = current_vowels_count = 0

            # while i < len(curr_window):
            #     if curr_window[i] in vowels:
            #         current_vowels_count += 1
            #     i += 1
            # max_vowels_count = max(max_vowels_count, current_vowels_count)  

            # time complexity could be improved to O(n) by using a sliding window

            #  avoid the need to check all k characters for each window, and would instead  only check the characters entering and leaving the window.

        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowels_count += 1
            if s[i-k] in vowels:
                current_vowels_count -= 1
            max_vowels_count = max(max_vowels_count, current_vowels_count)

        return max_vowels_count


            
