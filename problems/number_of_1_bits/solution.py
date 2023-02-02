class Solution:
    def hammingWeight(self, n: int) -> int:

        # Neetcode soln copy

        count = 0
        while n:
            count += n % 2

            # right shift by 1, so to ignore last bit everytime
            n = n >> 1
        return count