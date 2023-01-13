class Solution: 
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # string_list = []
        # def permute(s, result = ''):
        #     if (len(s) == 0):
        #         string_list.append(result)
        #         return
     
        #     for i in range(len(s)):
        #         ch = s[i]
        #         left_substr = s[0:i]
        #         right_substr = s[i + 1:]
        #         remaining = left_substr + right_substr
        #         permute(remaining, result + ch)

        # permute(s1)

        # for string_ in string_list:
        #     if string_ in s2:
        #         return True
        # return False


        s1_dict = collections.Counter(s1)
        s1_length = len(s1)
    
        s2_dict = collections.Counter(s2[:s1_length])
        
        if s1_dict == s2_dict:
            return True
        
        for i in range(len(s2) - s1_length):
            s2_dict[s2[i]] -= 1
            s2_dict[s2[i + s1_length]] += 1   
                
            if s1_dict == s2_dict:
                # print(s1_dict, s2_dict)
                return True
        return False