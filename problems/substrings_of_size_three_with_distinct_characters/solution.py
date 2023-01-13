class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        count = 0

        for index in range(len(s) - 2):
            if s[index] in s[index+1:index+3] or s[index+1] == s[index+2]:
                continue
            else:
                count += 1

        return count