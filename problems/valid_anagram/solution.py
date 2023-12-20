class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        str_dict = {}
        
        for ch in s:
            str_dict[ch] = str_dict.get(ch, 0) + 1

        for ch in t:
            if ch in str_dict and str_dict[ch] > 0:
                str_dict[ch] -= 1
            else:
                return False

        return sum(str_dict.values()) == 0


        # for x in s:
        #     if not x in t:
        #         return False
        #     t = t.replace(x, "", 1)
        # if len(t) == 0:
        #     return True
        # return False