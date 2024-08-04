class Solution:
    def fib(self, n: int) -> int:


        if n < 2:
            return n

        n1 = 0
        n2 = 1

        fn = 0
        for num in range(2, n + 1):
            fn = n1 + n2
            n1 = n2
            n2 = fn

        return fn
        
        