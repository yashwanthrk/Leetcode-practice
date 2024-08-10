class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
 
        count_dict = {}
        
        for ch1, ch2 in zip(s, t):
            count_dict[ch1] = count_dict.get(ch1, 0) + 1
            count_dict[ch2] = count_dict.get(ch2, 0) - 1

        
        for ch, count in count_dict.items():
            if count != 0:
                return False

        return True