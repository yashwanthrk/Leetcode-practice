class Solution:
    def isHappy(self, n: int) -> bool:
        

        seen = set()

        def happy_loop(n):

            n = str(n)
            total = sum([int(ch) * int(ch) for ch in n])

            if total == 1:
                return True

            elif total in seen:
                return False

            else:
                seen.add(total) 
                return happy_loop(total)
        
        return happy_loop(n)



        # seen = set()

        # while n != 1 and n not in seen:
        #     seen.add(n)
        #     n = sum(int(ch) ** 2 for ch in str(n))

        # return n == 1

            