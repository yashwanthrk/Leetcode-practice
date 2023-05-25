class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_dict = {}
        for x in s:
            str_dict[x] = str_dict.get(x, 0) + 1

        for x in t:
            if x in str_dict and str_dict[x] > 0:
                str_dict[x] -= 1
            else:
                return False

        if sum(str_dict.values()) == 0:
            return True

        return False

        # for x in s:
        #     if not x in t:
        #         return False
        #     t = t.replace(x, "", 1)
        # if len(t) == 0:
        #     return True
        # return False
