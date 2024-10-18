class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        from collections import Counter

        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False
        
        s1_dict = Counter(s1)
        s2_dict = Counter(s2[:s1_len])

        if s1_dict == s2_dict:
            return True


        for i in range(s2_len - s1_len):
            s2_dict[s2[i]] -= 1
            s2_dict[s2[i + s1_len]] += 1

            if s1_dict == s2_dict:
                return True

        return False

      