class Solution:
    def trailingZeroes(self, n: int) -> int:

        # 5! - one trailing zero
        # 10! - two trailing zero

        # 25! -  6 trailling zero
        #  25 // 5 ==> 5
        #  5 // 5  ==> 1 trailling zero

        result = 0

        while n >= 5:
            n = n // 5
            result += n

        return result 
        