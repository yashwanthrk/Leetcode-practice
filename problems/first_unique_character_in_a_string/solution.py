class Solution:
    def firstUniqChar(self, s: str) -> int:

        dict_ch = {}
        for ch in s:
            dict_ch[ch] = 1 + dict_ch.get(ch, 0)
        
        for index, ch in enumerate(s):
            if dict_ch[ch] == 1:
                return index
        
        return -1


        