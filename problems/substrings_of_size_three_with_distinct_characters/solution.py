class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        # if len(s) <= 2:
        #     return 0

        # count = 0
        # for i in range(len(s) - 2):
        #     cur_sub = s[i:i+3]
        #     if len(set(cur_sub)) == 3:
        #         count += 1

        # return count 


        count = 0
        for i in range(len(s) - 2):
            if s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2]:
                count += 1
        return count

            


