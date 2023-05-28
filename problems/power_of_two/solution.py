class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        def check_divisible_by_two(n):
            if n == 0:
                return False
                 
            if n == 1:
                return True
            
            if n % 2 == 0:
                return check_divisible_by_two((n // 2))

            return False


        return check_divisible_by_two(n)