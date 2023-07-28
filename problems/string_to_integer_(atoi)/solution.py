class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  
        if not s: 
            return 0  
        
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1

        # read until the next non-digit char
        i = 0
        while i < len(s) and s[i].isdigit():
            i += 1

        # convert to int
        num = s[:i]
        if not num:
            return 0
        else:
            num = int(num) * sign

        # clamp the number to be within the int range
        num = max(min(num, 2**31 - 1), -2**31)

        return num
