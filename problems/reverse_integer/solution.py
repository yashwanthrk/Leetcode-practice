class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1  
        INT_MIN = -2**31     

        # Handle negative numbers by storing the sign and using absolute value
        sign = -1 if x < 0 else 1
        x *= sign
        
        reversed_x = int(str(x)[::-1])
        
        if reversed_x > INT_MAX:
            return 0
        
        return sign * reversed_x