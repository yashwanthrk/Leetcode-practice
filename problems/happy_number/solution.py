class Solution:
    
    def isHappy(self, n: int) -> bool:
        
        # def check_happy_number(n):
        #     print(n)
        #     if n > 1 and n < 7 or n in [8, 9]:
        #         return False

        #     if n == 1 or n == 7:
        #         return True

        #     # n = str(n)
        #     # sum = 0
        #     # for x in n:
        #     #     sum += (int(x) ** 2)
        #     n = str(n)
        #     sum_val = sum(int(x) ** 2 for x in n)
           
        #     return check_happy_number(sum_val)

        # return check_happy_number(n)
        
        # use set to store the numbers that was found in the iteration
        # inc = set()

        # while (n not in inc) and n != 1:
        #     inc.add(n)
        #     res = 0 # number to store temporary sum
        #     while n:
        #         res += (n % 10) ** 2
        #         n = (n // 10)
        #     n = res
        
        # return True if n == 1 else False



        # def recursive_call(n, loop_dict):
            
        #     n = str(n)
            
        #     if n in loop_dict:
        #         return False
        #     else:
        #         loop_dict[n] = True

        #     sum = 0
        #     for num in (n):
        #         num = int(num)
        #         sum += (num * num)
    
    
    
        #     if sum == 1:
        #         return True
        #     else:
        #         # reapeat the recursion
        #         # check if its the infinite loop
        #         return recursive_call(sum, loop_dict)
        # return recursive_call(n, {})


        def get_next(num):
            return sum(int(digit) ** 2 for digit in str(num))

        # Create a slow pointer (tortoise) and a fast pointer (hare).
        
        tortoise = n
        hare = get_next(n)
        
        while hare != 1 and hare != tortoise:
            tortoise = get_next(tortoise)
            hare = get_next(get_next(hare))  # Move hare two steps.
            
        return hare == 1