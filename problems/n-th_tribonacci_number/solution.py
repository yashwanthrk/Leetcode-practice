class Solution:
    def tribonacci(self, n: int) -> int:

        def find_number(n, cache = {}):
            if n in cache:
                return cache[n]
            if n == 0:
                cache[n] = 0
                return 0
            if n in [1, 2]:
                cache[n] = 1
                return 1
            cache[n] =  find_number(n-3) + find_number(n-2) + find_number(n-1)
            return cache[n]

        return find_number(n)