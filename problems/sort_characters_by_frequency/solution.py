class Solution:
    def frequencySort(self, s: str) -> str:


        dict_s = {}

        for ch in s:
            dict_s[ch] = dict_s.get(ch, 0) + 1
        
        sorted_dict_s = dict(sorted(dict_s.items(), key=lambda x: x[1],reverse=True ))


        # new_s = ""
        # for key, value in sorted_dict_s.items():
        #     while value > 0:
        #         new_s += key
        #         value -= 1
    

        new_s = ''.join([ch * dict_s[ch] for ch in sorted_dict_s])

        return new_s

        