class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_dict  = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
             "IV": 4,
            "IX": 9,
            "XL": 40, 
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        # I can be placed before V (5) and X (10) to make 4 and 9.    
        # X can be placed before L (50) and C (100) to make 40 and 90. 
        # C can be placed before D (500) and M (1000) to make 400 and 900.

       
        result = 0
        
        i = 0
        while i < len(s):
            # This is the subtractive case.
            if i < len(s) - 1 and s[i:i+2] in roman_to_int_dict:
                result += roman_to_int_dict[s[i:i+2]]
                i += 2 
                 # Incrementing i by 1 to skip the next character in the subtractive case
            else:
                result += roman_to_int_dict[s[i]]
                i += 1

        return result




        # h = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "Z":0}
        # total = 0
        # s = s + 'Z'
        # for i in range(len(s)-1):
        #     if h[s[i]] < h[s[i+1]]:
        #         total -= h[s[i]]
        #     else:
        #         total += h[s[i]]
        # return total