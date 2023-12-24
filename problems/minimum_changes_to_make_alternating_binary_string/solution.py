class Solution:
    def minOperations(self, s: str) -> int:
        
        n = len(s)
        starts_with_zero = 0
        starts_with_one = 0

        for i in range(n):
            ch = int(s[i])
            if ch == i % 2:
                starts_with_zero += 1
            else:
                starts_with_one += 1

        return min(starts_with_zero, starts_with_one)