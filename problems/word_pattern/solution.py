class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # s = s.split(" ")

        # if len(pattern) != len(s):
        #     return False
        
        # map_p_s = {}
        # seen = set()

        # for i in range(len(pattern)):
        #     if pattern[i] in map_p_s:
        #         if s[i] != map_p_s[pattern[i]]:
        #             return False
        #     else:
        #         if s[i] in seen:
        #             return False
        #         map_p_s[pattern[i]] = s[i]
        #         seen.add(s[i])
        # print(map_p_s)
        # return True


        s = s.split()

        map_p_s = {}
        seen = set()

        for char, word in zip(pattern, s):
            if char in map_p_s:
                if word != map_p_s[char]:
                    return False
            else:
                if word in seen:
                    return False
                map_p_s[char] = word
                seen.add(word)

        return len(pattern) == len(s)
