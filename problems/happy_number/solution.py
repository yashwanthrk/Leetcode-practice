class Solution:
    def isHappy(self, n: int) -> bool:
        

        cycle_set = set()

        def check_for_happy_number(n):

            if n in cycle_set:
                return False
            
            cycle_set.add(n)

            if n == 1:
                return True
            
            num_ = 0
            for ch in str(n):
                num_ += int(ch) * int(ch)

            print(num_)

            return check_for_happy_number(num_)

        return check_for_happy_number(n)
