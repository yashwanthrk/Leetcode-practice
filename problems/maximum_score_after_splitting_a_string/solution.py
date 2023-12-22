class Solution:
    def maxScore(self, s: str) -> int:

        zero_count = 0
        result = 0 
        one_count = s.count("1")



        for i in range(len(s) - 1):
            if s[i] == "1":
                #         If s[i] == '1': this 1 was in the right part, but it is now joining the left part. Thus, we lose 1 score since the right part is losing a 1. Decrement ones.
                one_count -= 1
            else:
                # If s[i] == '0', this 0 was in the right part, but it is now joining the left part. Thus, we gain 1 score since the left part is gaining a 0. Increment zeros.

                zero_count += 1
        
            result = max(result, zero_count + one_count)
        
        return result


        