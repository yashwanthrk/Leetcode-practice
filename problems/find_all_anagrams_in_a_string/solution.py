from collections import Counter

class Solution:
    
    # error - Time Limit Exceeded

    # def check_anagram_cond(self, s1, s2):
    #     return Counter(s1) == Counter(s2)
    #     # return ''.join(sorted(s1)) == ''.join(sorted(s2))

    def findAnagrams(self, s: str, p: str) -> List[int]:

    #     p_length = len(p)
    #     anagaram_indexes = []

    #     if len(s) < p_length:
    #         return anagaram_indexes

    #     for index in range(len(s) - p_length + 1):
    #         current_str = s[index:index + p_length]
    #         if len(current_str) == p_length and self.check_anagram_cond(current_str, p):
    #             anagaram_indexes.append(index)
                
    #     return anagaram_indexes

    # neet code

        s_len = len(s)
        p_len = len(p)
        
        if s_len < p_len: 
            return []

        s_map = {}
        p_map = {}
        for i in range(p_len):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            p_map[p[i]] = p_map.get(p[i], 0) + 1


        result = []
        if s_map == p_map:
            # start index
            result.append(0)


        first_ptr = 0
        for last_ptr in range(p_len, s_len):
            # increase window size
            s_map[s[last_ptr]] = s_map.get(s[last_ptr], 0) + 1
            
            # decrease window size
            s_map[s[first_ptr]] -= 1

            if s_map[s[first_ptr]] == 0:
                s_map.pop(s[first_ptr])

            first_ptr += 1

            if s_map == p_map:
                result.append(first_ptr)

        return result 


            
        
            
