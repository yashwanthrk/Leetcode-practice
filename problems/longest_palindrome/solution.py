class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_dict = collections.Counter(s)
        count = 0
        check_for_single_char = True
        for ch in count_dict:
            if count_dict[ch] > 1:
                count += (count_dict[ch] // 2) * 2 
                count_dict[ch] = count_dict[ch] - (count_dict[ch] // 2) * 2
            if count_dict[ch] == 1 and check_for_single_char:
                count += 1
                check_for_single_char = False
        return count
        
